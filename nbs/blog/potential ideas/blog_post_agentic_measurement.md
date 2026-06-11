# When the Loop Runs But the Paper Doesn't Improve: A Measurement Problem in Agentic AI

*A neuroscientist's field notes on building LLM workflows, unexpected teachers, and why evaluation is harder than it looks.*

---

## The Seductive Simplicity

I thought this would be easy.

The task: turn a novel data visualization method into a short, rigorous methods paper suitable for a computational statistics journal. The method is Whorl Maps, a visualization technique I co-developed for [DABEST](https://github.com/ACCLAB/DABEST-python) — an open-source statistical estimation framework with 2,000+ citations. The code is already written. The method is mathematically straightforward. The motivation is documented in fragments across feature tutorials and design notes. We have guiding principles from Tufte. We have a clear target — a methods paper, not a science paper, so the reasoning requirements are relatively contained. There is no fraught causal inference chain to defend, no clinical implications to hedge. Just: here is a visualization, here is why it works, here is how to use it.

Scope is restricted. Target is defined. Code is the spec. Literature is tractable — data visualization papers are not quantum gravity. I even have the journal in mind.

This seemed like exactly the kind of task agentic LLM workflows are built for.

---

## The Initial Design

The initial design was straightforward, in the way that initial designs always are.

A LangGraph loop with multiple specialized agents, each evaluating the draft on a specific dimension: scientific integrity, methodological precision, journal fit, clarity for the target audience. Each agent scores its dimension. Scores are tracked across iterations. The loop continues until scores converge above threshold, or a human intervenes. Progress is measurable. Quality is operationalized. The system knows when it's done.

I workshopped the prompt architecture with Claude — which, for anyone who hasn't used it extensively, is genuinely excellent at careful reasoning, thorough code review, and thinking through edge cases. Claude Code then laid out a project structure and loop workflow quickly and cleanly.

For a sanity check, I handed the workflow to GPT — at this point I was still primarily a Claude user, and I wanted a second opinion before committing to a production loop. GPT's response surprised me.

It didn't critique the prompt logic or the agent roles. It flagged the architecture. A production loop running upfront, without phasing, could run away quickly into expensive corners — iterating on a draft that wasn't ready to be iterated on, burning tokens optimizing local problems while the global structure remained broken. It suggested a phasing strategy: establish document architecture and scope before entering the refinement loop.

I was genuinely taken aback. Not because the advice was revolutionary — it wasn't — but because I hadn't asked that question, and Claude hadn't volunteered it. GPT had looked at the workflow and immediately asked: *what happens when this goes wrong?*

That was the first inkling that the two models were optimized differently. Claude reasons carefully within a frame. GPT interrogates the frame. Both are useful. Using them interchangeably wastes the difference.

---

## The Unexpected Teacher

This asymmetry became the organizing principle of the current workflow.

One model — Claude — handles execution: code, implementation, local edits, responding to specific critique. The other — GPT — acts as structural manager: interrogating the paper architecture, tightening evaluation criteria, identifying where the automation loop itself needs guardrails before I let it run.

The separation is now explicit and deliberate:

- **Execution engine:** implement, edit, respond, generate
- **Structural auditor:** interrogate scope, tighten criteria, identify failure modes in the workflow itself

A few concrete improvements came directly from this division:

The draft was reframed as a strict methods paper, not a general introduction to estimation statistics. Vague scientific language — the kind that sounds rigorous but commits to nothing — was flagged and tightened into precise, testable claims. Evaluation criteria shifted from subjective "journal fit" toward article-type fit using reference papers as ground-truth constraints. Repair steps were tied to diagnostic metrics rather than unconstrained rewriting. And human intervention points became explicit: agents can propose changes to protected claims, citation choices, or core framing, but cannot silently rewrite them.

That last point kept coming back to me.

---

## Why Human Checkpoints Are Not Safety Theater

The explicit human intervention points started as a practical guardrail — a way to prevent the loop from silently drifting away from scientific intent. Over time I've come to think they're something more fundamental.

"Is this sentence clear?" has no ground truth without a reader who knows the field, the journal, and the surrounding argument. Style, scientific register, precision of claim — none of these can be evaluated without a human in the loop to define what *correct* means in this specific context.

This is not a limitation of current models that will be engineered away. It is an epistemological fact about open-ended, domain-specific quality. The evaluation requires judgment that is constitutively human and contextual.

Which brings me to the harder question I've been sitting with.

---

## The Measurement Problem

Does this two-model asymmetric loop actually improve the paper?

That question is not on any benchmark.

To be clear: we have rigorous benchmarks for LLM capabilities. MMLU, GPQA, HumanEval, BIG-Bench, MATH — these measure what individual models can do on standardized, closed-ended tasks with ground-truth answers. That is real and valuable science. The cognitive faculty decomposition work being done at Anthropic, Google DeepMind, and elsewhere is genuinely sophisticated.

But these benchmarks measure *single models* on *single capabilities* on *simplex tasks with known answers*. They do not — and by design cannot — measure whether a multi-model agentic workflow improves a complex, open-ended, domain-specific artifact over multiple iterations.

For that question, the ground truth is expert scientific judgment. The evaluation metric is... undefined. We have scores — journal fit: 7.2/10, scientific integrity: 8.1/10 — but what do those numbers mean? Are they measuring anything that correlates with what a methods editor at a computational statistics journal would actually accept?

I genuinely don't know. And I've been thinking about this problem for fifteen years in a different domain.

---

## I've Seen This Failure Mode Before

In 2017, my lab published a paper establishing that dorsal raphe serotonergic neurons control intertemporal choice in rodents. In 2019, I started building DESTRA — a benchmarking framework for high-dimensional behavioural states in *Drosophila* — because I kept seeing a specific failure mode in the circuit neuroscience literature.

The failure mode: circuit manipulations that appeared successful on individual behavioural metrics turned out, under multidimensional evaluation, to have failed to reproduce the underlying target state.

Concretely: if you activate a neuron population and measure feeding volume, and feeding volume increases, you might conclude you've made the fly hungrier. But if you measure the full behavioural signature — feeding rate, meal duration, locomotion pattern, port occupancy, post-meal walking speed, and fourteen other metrics — and compare that signature against the natural profile of a genuinely hungry fly, you often find that the manipulation produced something that *looked like* hunger on one dimension while diverging substantially from hunger on every other.

The single metric was optimized. The underlying state was not reproduced.

DESTRA [Science Advances, in revision] exists to catch this. Instead of evaluating manipulations against individual metrics, it compares the full multidimensional behavioural signature against empirically-defined ground truth — the natural hunger-satiety transition — and quantifies "state-likeness" as a holistic measure.

The agentic workflow failure mode is structurally identical.

A loop can run productively — drafts generated, critiques applied, scores incrementing — while the thing we actually care about (scientific quality, argument coherence, claim precision, appropriate scope) drifts in an unmeasured direction. The loop optimizes its metrics. The target state remains unevaluated.

---

## What the Solution Space Looks Like

In neuroscience, the solution required:

1. Defining the target state empirically, not by assumption
2. Measuring against the full multidimensional signature, not individual metrics
3. Using bootstrap-derived confidence intervals to give honest uncertainty estimates on the comparison
4. Building in expert validation at points where judgment is constitutively required

The analogous framework for agentic scientific writing evaluation would look something like:

1. **Ground-truth-referenced benchmarks:** use accepted papers in the target journal as empirical reference states, not abstract rubrics
2. **Multidimensional evaluation:** score across dimensions that genuinely matter for acceptance — argument structure, claim precision, citation appropriateness, methodological transparency — not proxies
3. **Bootstrap confidence intervals over expert ratings:** rather than point scores, estimate the distribution of expert judgment using resampling, giving honest uncertainty on quality estimates
4. **Inter-rater agreement measurement:** use Cohen's Kappa or similar to validate that evaluation criteria are being applied consistently before trusting the scores
5. **Bias correction for imperfect judges:** apply Rogan-Gladen or similar estimators when LLM judges are used as proxies for human expert judgment

None of this exists as a standard framework for agentic scientific writing. Most workflows rely on LLM self-evaluation, which is a known reliability problem, or human intuition, which doesn't scale.

The real opportunity may not be using AI to write or code faster. It may be designing measurable systems for deciding when AI work is actually improving — and being honest about what we don't yet know how to measure.

---

## Where This Leaves Me

The Whorl Maps methods paper is better than when I started. The asymmetric workflow helped. The explicit human checkpoints helped more than I expected.

But I can't tell you *how much* better it is, or whether the improvement will survive peer review, or whether a different workflow would have done better. I have scores, not evidence.

This is an uncomfortable position for someone who built a 2,000-citation framework specifically to stop scientists from reporting numbers they can't interpret. It suggests the next interesting problems in agentic AI are not in the models.

They are in the evaluation frameworks we build around them.

---

*Sangyu Xu is a computational behaviour scientist and AI evaluation researcher relocating to Boston in September 2026. She is co-lead of [DABEST 2.0](https://github.com/ACCLAB/DABEST-python) (Nature Methods, in revision) and developer of DESTRA, a benchmarking framework for high-dimensional behavioural states.*

*This post describes work in progress. The Whorl Maps paper and the evaluation framework are both under active development.*
