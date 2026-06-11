# Reasoning Rubrics: LLM Workflows as a Medium for Transferring Scientific Writing Intuition

**Prepared:** 2026-06-10  
**Model / mode:** GPT-5.5 Thinking  
**Status:** Short conceptual draft

---

## Core idea

Scientific writing is often taught through repeated correction rather than explicit instruction. Senior scientists develop a strong intuitive sense for what makes a paper work: whether the main claim is proportionate, whether the figure carries the argument, whether a limitation is honest or overdefensive, whether the Introduction frames the real problem, and whether the manuscript reads like the right article type. Yet much of this judgment is tacit. It is learned by drafting, being corrected, revising, and gradually absorbing expert taste.

Journals already provide style guidelines: word limits, section formats, citation rules, figure requirements, data-availability statements, and reporting checklists. But these are mostly surface-level constraints. They tell authors how a paper should look. They rarely explain how a paper should think.

The missing object is the reasoning rubric.

A reasoning rubric captures the deeper editorial and scientific judgments that senior scientists routinely apply but rarely formalize. These include rhetorical hierarchy, claim safety, figure-as-argument logic, reviewer theory-of-mind, article-type fit, proportionality of caveats, novelty framing, and the distinction between central claims and minor implementation details.

LLM-mediated manuscript workflows create a new opportunity to externalize these rubrics. When a senior scientist corrects an LLM writing or review workflow, the correction can be converted into a reusable artifact: a labeled example, a scoring criterion, a repair pattern, a decision gate, or a ground-truth annotation. Over time, the workflow becomes more than a writing assistant. It becomes a structured record of expert reasoning.

This reframes the role of a tuned manuscript agent. The point is not simply that LLMs can write prose, provide feedback, or imitate reviewers. Those capacities are already clear. The more interesting possibility is that a senior scientist can use the workflow to teach the system what counts as good scientific judgment. In doing so, the scientist is forced to verbalize intuitions that would otherwise remain implicit.

The resulting artifacts can support junior scientists in a way that ordinary style guides cannot. A junior scientist can learn not only that a paragraph should be shorter, but why it is overdefended; not only that a figure should be revised, but whether it is failing to carry the central argument; not only that a claim is unsafe, but how to make it precise without making it dull. This is closer to cognitive apprenticeship than automated writing.

In this view, a manuscript workflow is a medium for transferring tacit expertise. Senior intuition becomes critique; critique becomes rubric; rubric becomes examples; examples become judge behavior; judge behavior becomes repair planning; and repair planning becomes reusable pedagogy.

A useful slogan is:

> Style guides tell you how a paper should look. Reasoning rubrics tell you how a paper should think.

---

## Key claims

1. **Scientific writing expertise is partly tacit.**  
   Senior scientists often know when a manuscript is overclaiming, underclaiming, misframed, overdefended, or structurally wrong before they can easily state the rule.

2. **Existing journal guidance is mostly stylistic and procedural.**  
   Journals specify format, length, citation style, figure requirements, and reporting norms, but they rarely encode the reasoning patterns behind strong scientific argumentation.

3. **LLM workflows force tacit judgment to become explicit.**  
   To make a manuscript agent useful, the expert must define what good judgment looks like: what counts as proportional, novel, safe, persuasive, article-appropriate, and reviewer-resilient.

4. **Rubrics and ground-truth examples are the key transfer objects.**  
   The valuable artifacts are not just prompts, but labeled examples, critique patterns, repair rules, scoring criteria, and intervention gates.

5. **The goal is not replacing mentorship but making mentorship more durable.**  
   A tuned workflow can preserve repeated acts of expert correction so that junior scientists can learn from them across drafts, projects, and manuscripts.

---

## Example reasoning rubrics

- **Rhetorical hierarchy:** Does the manuscript give paragraph-level weight to major claims and sentence-level weight to minor caveats?
- **Claim safety:** Is the claim scientifically defensible without becoming so cautious that it loses force?
- **Figure-as-argument:** Does each figure prove a necessary point in the manuscript’s logic?
- **Article-type fit:** Does the paper read like the kind of paper it is trying to be?
- **Proportionality of limitations:** Is a limitation honestly acknowledged without becoming the center of the paper?
- **Reviewer theory-of-mind:** What objection would a careful reviewer raise, and has the paper answered it at the right level?
- **Implementation-detail demotion:** Are technical parameters explained without being rhetorically overpromoted?
- **Novelty framing:** Is the contribution positioned as a real missing object rather than a repackaging of known tools?

---

## Possible title directions

- **Reasoning Rubrics: LLM Workflows as a Medium for Transferring Scientific Writing Intuition**
- **Style Guides Tell Papers How to Look; Reasoning Rubrics Tell Them How to Think**
- **From Tacit Mentorship to Executable Rubrics**
- **LLM-Mediated Cognitive Apprenticeship for Scientific Writing**
- **Can a Manuscript Agent Teach Scientific Taste?**

---

## One-sentence version

LLM-mediated manuscript workflows can convert senior scientists’ tacit writing and reasoning intuition into explicit reasoning rubrics, labeled examples, and decision gates, creating a reusable medium for transferring scientific judgment that conventional journal style guides do not provide.
