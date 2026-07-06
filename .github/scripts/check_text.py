"""
Text originality checker.

Free tier: rolling-hash verbatim detection (catches exact/near-exact copying of
paragraphs ≥ 40 words). Fails on any match above the similarity threshold.

Paid tier: Copyleaks API web check. Set COPYLEAKS_API_KEY and COPYLEAKS_EMAIL
secrets in GitHub repo settings to enable. 250 free credits/month on dev plan.
"""

import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

# Similarity threshold for internal verbatim detection (0–100).
# 85 = 85% of 5-word shingles match → flag as suspicious.
SHINGLE_THRESHOLD = 85
MIN_WORDS = 40  # paragraphs shorter than this are skipped


def extract_text_blocks(path: Path) -> list[str]:
    """Extract prose paragraphs from qmd/md/txt/ipynb files."""
    content = path.read_text(errors="ignore")

    if path.suffix == ".ipynb":
        try:
            nb = json.loads(content)
            blocks = []
            for cell in nb.get("cells", []):
                if cell.get("cell_type") == "markdown":
                    blocks.append("".join(cell["source"]))
            content = "\n\n".join(blocks)
        except json.JSONDecodeError:
            pass

    # Strip YAML frontmatter
    content = re.sub(r"^---.*?---\s*", "", content, flags=re.DOTALL)
    # Strip HTML/code blocks
    content = re.sub(r"```.*?```", "", content, flags=re.DOTALL)
    content = re.sub(r"<[^>]+>", " ", content)

    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", content)]
    return [p for p in paragraphs if len(p.split()) >= MIN_WORDS]


def shingle(text: str, k: int = 5) -> set[str]:
    words = text.lower().split()
    return {" ".join(words[i : i + k]) for i in range(len(words) - k + 1)}


def similarity(a: str, b: str) -> float:
    sa, sb = shingle(a), shingle(b)
    if not sa or not sb:
        return 0.0
    return 100 * len(sa & sb) / len(sa | sb)


def check_internal_duplication(blocks: list[tuple[str, str]]) -> list[str]:
    """Check for near-duplicate paragraphs across all collected blocks."""
    violations = []
    seen = []  # (text, source_label)
    for text, label in blocks:
        for prev_text, prev_label in seen:
            if prev_label == label:
                continue  # skip same-file comparison
            score = similarity(text, prev_text)
            if score >= SHINGLE_THRESHOLD:
                snippet = " ".join(text.split()[:12])
                violations.append(
                    f"  [{score:.0f}% match] '{snippet}…'\n"
                    f"    in {label}\n"
                    f"    vs {prev_label}"
                )
        seen.append((text, label))
    return violations


def check_copyleaks(text: str, label: str) -> list[str]:
    """Submit text to Copyleaks API. Returns violation strings."""
    import requests

    api_key = os.environ.get("COPYLEAKS_API_KEY", "")
    email = os.environ.get("COPYLEAKS_EMAIL", "")
    if not api_key or not email:
        return []

    violations = []
    try:
        # Authenticate
        auth = requests.post(
            "https://id.copyleaks.com/v3/account/login/api",
            json={"email": email, "key": api_key},
            timeout=30,
        )
        auth.raise_for_status()
        token = auth.json()["access_token"]

        scan_id = hashlib.md5(label.encode()).hexdigest()[:16]
        headers = {"Authorization": f"Bearer {token}"}

        # Submit
        requests.put(
            f"https://api.copyleaks.com/v3/businesses/submit/file/{scan_id}",
            headers=headers,
            json={
                "base64": __import__("base64").b64encode(text.encode()).decode(),
                "filename": f"{scan_id}.txt",
                "properties": {"webhooks": {}, "sensitiveDataProtection": True},
            },
            timeout=30,
        ).raise_for_status()

        # Poll for result (max 90s)
        for _ in range(18):
            time.sleep(5)
            result = requests.get(
                f"https://api.copyleaks.com/v3/businesses/{scan_id}/result",
                headers=headers,
                timeout=30,
            )
            if result.status_code == 200:
                data = result.json()
                score = data.get("scannedDocument", {}).get("matchedPercent", 0)
                if score >= 20:
                    violations.append(
                        f"  Copyleaks: {score:.0f}% match against web sources in {label}"
                    )
                break
    except Exception as e:
        print(f"  [Copyleaks] skipped ({e})")

    return violations


def main(changed_files_path: str) -> int:
    try:
        changed = Path(changed_files_path).read_text().splitlines()
    except FileNotFoundError:
        print("No changed files list found — skipping text check.")
        return 0

    changed = [f.strip() for f in changed if f.strip()]
    if not changed:
        print("No text files changed.")
        return 0

    all_blocks: list[tuple[str, str]] = []
    for fpath in changed:
        p = Path(fpath)
        if not p.exists():
            continue
        blocks = extract_text_blocks(p)
        for b in blocks:
            all_blocks.append((b, fpath))

    if not all_blocks:
        print("No prose blocks found in changed files.")
        return 0

    print(f"Checking {len(all_blocks)} prose blocks from {len(changed)} file(s)…")
    violations = check_internal_duplication(all_blocks)

    # Copyleaks check (only if API key set)
    if os.environ.get("COPYLEAKS_API_KEY"):
        for text, label in all_blocks:
            violations.extend(check_copyleaks(text, label))

    if violations:
        print("\n❌ Text originality violations found:\n")
        for v in violations:
            print(v)
        return 1

    print("✅ No text originality issues detected.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "changed_files.txt"))
