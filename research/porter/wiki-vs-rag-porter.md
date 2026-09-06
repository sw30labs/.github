# Wiki vs RAG — Porter Five Forces

6 September 2026. Analyst assessment; 1 = low pressure, 5 = very high. Read with the portfolio report for scope, assumptions and weekly allocation.

## Wiki vs RAG

**Current state:** Evidence-selected flagship; four-arm study on one corpus.

**Market boundary:** Reproducible retrieval-strategy comparisons for builders selecting knowledge workflows.

**Confidence:** Medium for recorded comparison; low external validity.

**Rivalry — 4/5 (High).** Ragas and Promptfoo already support evaluation workflows. The useful contribution is a transparent comparison and dataset, not another evaluation product.

**Supplier power — 3/5 (Moderate).** Embedding models, generators and judges influence rankings. Open tooling offers alternatives, but upgrades can change comparability.

**Buyer power — 4/5 (High).** Builders need results on their own corpus. A single-corpus conclusion transfers poorly, giving potential adopters strong reasons to rerun or ignore it.

**Threat of entrants — 5/5 (Very high).** A comparison notebook is cheap to create. High-quality human labels, repeated runs and independently reproducible costs are harder to establish.

**Threat of substitutes — 5/5 (Very high).** Small hand-labeled tests, existing evaluation libraries and pragmatic single-shot retrieval can answer the decision without a separate project.

**Grounding:** [Ragas](https://github.com/vibrantlabsai/ragas), [Promptfoo](https://github.com/promptfoo/promptfoo), [Wiki vs RAG repository](https://github.com/sw30labs/wiki-vs-rag). Ratings and competitive implications above are analyst inferences from these sources.

**Defensible direction to test:** Decision-grade tradeoffs with explicit uncertainty and full indexing, retrieval and generation costs.

**Standalone decision:** Repeat the frozen study and add a second corpus.

**Holistic amendment:** Treat it as reusable Research Engine methodology and a rotating publication asset. Do not duplicate an evaluation framework or infer a universal winner.

**Next human effort:** Audit a blinded sample of judge results; choose a second corpus that could reverse the original finding.

**Bounded Nightshift work:** Reproduce the frozen questions, capture failures and compute per-strategy distributions and confidence intervals.

**Promote / stop gate (proposed):** If rankings change materially across seeds or corpora, report conditional guidance. End the study when it supports an actionable retrieval choice.

