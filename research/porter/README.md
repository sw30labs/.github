# SW30 Labs — Porter Five Forces and weekly portfolio decisions

Assessment date: 6 September 2026. Purpose: allocate a solo researcher’s scarce attention while preserving the lab’s rate of ideas becoming evidence.

## Scope and method

Before this update, the organization profile featured nine projects, but does not classify all nine as FLAGSHIP. The pre-assessment public inventory had four FLAGSHIP rows (Loopscope, OSCAL Skills Guardrails, TSLIT-DSPy DGX and Wiki vs RAG); RPC-H16 is additionally a Frontier flagship. To avoid excluding your featured work, this assessment covers all nine profile projects plus Nightshift. Existing design/PoC labels are preserved. This landing-page edition adds Nightshift as a Research Engine flagship; this is an editorial designation, not a claim of measured productivity.

Porter’s framework evaluates industry structure: rivalry, suppliers, buyers, entrants and substitutes. Four surrounding forces plus rivalry in the center form the clickable diagram; these are not four business quadrants. The separate portfolio buckets express weekly decisions, not additional Porter forces. See [Harvard’s framework](https://www.isc.hbs.edu/strategy/business-strategy/Pages/the-five-forces.aspx).

Ratings are analyst judgments (1 low pressure, 5 very high pressure), not measured probabilities or market-share statistics. Market boundaries differ and early-stage projects have much lower confidence. The displayed mean is an equal-weight descriptive pressure summary, not a priority or profitability score. High barriers reduce entrant threat but can also obstruct SW30’s own entry. A project’s engineering maturity is not a Porter force.

General model knowledge supplies the reasoning about switching costs, entry barriers, substitutes and resource allocation; current product facts come from linked primary sources and live authenticated GitHub reads. Repository claims are not independently rerun results. Search indexes showed an older organization profile, so the live GitHub profile and dossiers were used for scope. No customer interviews, revenue records, fresh model evaluations or hardware benchmarks were performed. Commercial buyers are hypotheses where no adoption evidence exists.

## Portfolio decision after the holistic pass

Use Loopscope, Nightshift and OSCAL Skills Guardrails as the active core. The relationship is an opportunity to share a reference workflow, evidence and fixtures; it is not a completed governed platform. Count shared work once. Keep one rotating empirical study and one small frontier slot; the remaining projects stay visible without receiving a recurring build commitment.

Nightshift deserves a **Research Engine flagship** designation: a concrete, inspectable instrument that could amplify every program. Its first success criterion is net human time saved, not commits, token throughput, GPU utilization or self-improvement activity. Already-owned hardware is a sunk cost; idle machines do not justify low-value jobs. Net saved time = estimated manual time for accepted work minus briefing, review, repair and allocated maintenance time. Track uncertainty in the manual estimate and include failed runs. Energy cost is additional; no tariff saving was independently verified.

The most important amendments are: narrow Guardrails around content-bound evidence rather than dual-scanner novelty; protect Loopscope’s small local workflow; treat Wiki vs RAG as reusable methodology; keep TSLIT’s negative findings explicit; move VideoCortex away from a generic video market and account for its upstream noncommercial license; gate AI-OS-1 on measured need; defer AEGIS appliance development; keep RPC-H16 as a bounded research option; and judge Atlas by decisions changed rather than its index.

## A discrete 10-hour example week

This is a planning assumption, not your reported availability. Scale with the interactive budget control. At very small budgets, consolidate tasks rather than fragment every project into minutes.

| Work | Share | At 10 hours | Concrete output |
|---|---:|---:|---|
| Loopscope | 25% | 2.5 h | One reproducible diagnosis example and one user-friction fix |
| OSCAL Skills Guardrails | 20% | 2 h | Frozen acceptance cases and reviewed admission evidence |
| Nightshift | 15% | 1.5 h | Morning review, net-time ledger and one reliability bottleneck |
| Rotating study | 15% | 1.5 h | One finding; default Wiki vs RAG, then TSLIT, then VideoCortex |
| RPC-H16 | 10% | 1 h | One bounded geometry assumption or result |
| Singularity Atlas | 5% | 0.5 h | One sourced signal that changes a decision |
| Portfolio review / contingency | 10% | 1 h | Accept, defer or stop; close review backlog |

Nightshift’s 15% is human oversight/maintenance, not machine run time. Pilot two nights a week with one target and two bounded jobs, sequentially; permit more only after review capacity and measured usefulness support it. Focus nights on Loopscope/Guardrails or the selected study. Nightshift self-work is capped at one bounded reliability job per week. Its current recency/CMM selection is not strategic priority: manually select targets until a tested priority mechanism exists. Do not run performance benchmarks while the same hardware is serving coding jobs.

Below 6 hours/week, reserve review time, choose Loopscope plus either Guardrails or a live blocker, and rotate the other work across weeks. Above 10 hours, deepen the same experiments before activating more projects. Stop queuing nights when more than one morning review session is outstanding. The visualization scales shares as an illustration; this batching rule overrides tiny allocations.

## Sensitivity and review cadence

The default objective is research evidence plus useful tools. Under near-term revenue, put extra human time into outside-user discovery for Loopscope and Guardrails; do not equate their current rank with validated revenue. Keep Nightshift as internal capacity and lower frontier allocation. Under reputation, prioritize a reproducible study and publishable negative findings; Atlas supports distribution. No alternative ranking is asserted as objectively optimal without your preferences.

At the end of each week record accepted outputs, founder minutes, maintenance burden and the decision changed. Every two weeks apply each project’s gate. Move the rotating slot, rather than adding another commitment. If Nightshift creates net review debt, reduce runs before investing in more orchestration. If a clear user need appears for a gated project, replace an existing slot explicitly. Revisit competitor evidence monthly or before a substantial commitment; ratings dated today are not live telemetry.

## Individual assessments — final amended versions


## Loopscope

**Current state:** Owner-designated flagship; beta; daily personal use reported.

**Market boundary:** Local inspection and replay of agent workflows for individual builders and small research teams.

**Confidence:** Medium: usage attributed; market position inferred.

**Rivalry — 4/5 (High).** LangSmith and Langfuse already address tracing and evaluation. Their breadth raises the bar; Loopscope competes on setup burden and legibility of live loops, not trace-platform breadth.

**Supplier power — 3/5 (Moderate).** LangGraph and its event interfaces shape compatibility. Open source reduces contractual lock-in, but maintaining hooks through upstream changes still costs founder time.

**Buyer power — 4/5 (High).** Developers can choose free tools and readily replace a small hook. Daily personal use establishes internal utility; willingness to pay and independent adoption remain unmeasured.

**Threat of entrants — 4/5 (High).** A basic dashboard is easy to reproduce. Reliable replay, bounded overhead and clear nested-run behavior take more work, but are not yet a durable entry barrier.

**Threat of substitutes — 4/5 (High).** Console logs, JSONL inspection and framework-native traces can solve the immediate debugging job without another dashboard.

**Grounding:** [LangSmith observability](https://www.langchain.com/langsmith/observability), [Langfuse self hosting](https://langfuse.com/self-hosting), [Loopscope repository](https://github.com/sw30labs/loopscope). Ratings and competitive implications above are analyst inferences from these sources.

**Defensible direction to test:** A tiny, local, failure-tolerant instrument with a reproducible example of finding an otherwise costly failure.

**Standalone decision:** Make Loopscope the lead practical-tool flagship.

**Holistic amendment:** Keep it a lead, but use Nightshift as one demanding reference workflow. Do not build a second general observability platform. Internal integration is a testbed, not independent market validation.

**Next human effort:** Time one real diagnosis with and without replay; prepare a clean-install exercise for an outside user.

**Bounded Nightshift work:** One bounded replay or nested-run regression with a failing fixture, passing check and replay artifact.

**Promote / stop gate (proposed):** After two weekly cycles, retain development priority only if diagnosis time improves or an outside user completes the example and identifies a concrete need.


## Nightshift

**Current state:** Research Engine flagship; implemented local workflow; net time savings under evaluation.

**Market boundary:** Bounded overnight code maintenance across a solo builder’s repository portfolio.

**Confidence:** Medium on implementation; low on net savings and demand.

**Rivalry — 5/5 (Very high).** OpenHands and the broader coding-agent category compete for delegated development work. A writer/critic loop by itself is readily substitutable; the narrow portfolio contract is the stronger differentiator.

**Supplier power — 4/5 (High).** Useful output depends on model quality, serving stacks and local hardware. Separate writer and critic endpoints do not guarantee independent errors or effective criticism.

**Buyer power — 4/5 (High).** A solo developer can switch harnesses or work interactively. The relevant purchase decision is attention: every rejected branch and long review reduces value.

**Threat of entrants — 5/5 (Very high).** Open frameworks make it inexpensive to assemble overnight loops. A trustworthy record of accepted changes and measured review cost is harder to replicate than the interface.

**Threat of substitutes — 5/5 (Very high).** Interactive coding assistants, scripted maintenance and leaving low-value work undone can all outperform unattended work once review and repair time are counted.

**Grounding:** [OpenHands](https://github.com/OpenHands/OpenHands), [DwarfStar inference engine](https://github.com/antirez/ds4), [Nightshift repository](https://github.com/sw30labs/nightshift). Ratings and competitive implications above are analyst inferences from these sources.

**Defensible direction to test:** Frozen small briefs, host-verified checks, reviewable branches and useful cross-repository memory.

**Standalone decision:** Assess as a crowded coding-agent product with uncertain external demand.

**Holistic amendment:** Designate as a cross-cutting Research Engine flagship for internal capacity, while keeping commercial ambition conditional. Limit self-improvement so the engine does not consume the lab.

**Next human effort:** Review accepted outcomes and log minutes spent specifying, reviewing and repairing. Choose tasks by portfolio priority, not repository recency alone.

**Bounded Nightshift work:** Start with one target and two checkable jobs per night. Produce branch, test log, summary and accepted/rejected outcome; run sequentially on shared hardware.

**Promote / stop gate (proposed):** Over two weeks, require positive net human time saved and no material scope violation. Count failed and abandoned runs. Pause expansion if review backlog exceeds one morning session.


## OSCAL Skills Guardrails

**Current state:** Evidence-selected flagship; reference implementation with hardening gaps.

**Market boundary:** Policy-driven admission and integrity evidence for organizations adopting executable agent skills.

**Confidence:** Medium: artifacts inspected; enforcement and general detection unverified.

**Rivalry — 4/5 (High).** Cisco Skill Scanner already combines static, semantic and behavioral checks. Dual evidence alone is weak differentiation; policy linkage and content-bound decisions are the plausible niche.

**Supplier power — 3/5 (Moderate).** NIST OSCAL is a public data standard, reducing dependence on a proprietary schema. Scanner and judge changes still affect evidence consistency and maintenance.

**Buyer power — 4/5 (High).** Security teams demand demonstrable false-positive rates, enforcement and usable evidence. They can prefer existing scanners or postpone adoption; no paying design partner was evidenced.

**Threat of entrants — 4/5 (High).** Adding a policy wrapper is relatively easy. Robust mutation handling, digest-bound approvals and independently reproducible evaluation create a higher practical barrier.

**Threat of substitutes — 4/5 (High).** Manual skill review, allowlists, restricted execution and existing CI scanners can satisfy parts of the job. Admission scanning cannot substitute for runtime containment.

**Grounding:** [Cisco Skill Scanner](https://github.com/cisco-ai-defense/skill-scanner), [NIST OSCAL model overview](https://www.nist.gov/system/files/documents/2021/02/25/Day1.1-Michaela-OSCAL%20Overview.pdf), [OSCAL Skills Guardrails repository](https://github.com/sw30labs/oscal-skills-guardrails). Ratings and competitive implications above are analyst inferences from these sources.

**Defensible direction to test:** Reproducible, digest-bound admission decisions with inspectable OSCAL evidence, rather than a promise of universal detection.

**Standalone decision:** Prioritize hardening and a clean/adversarial evaluation over feature growth.

**Holistic amendment:** Retain as the primary security experiment. Reuse a bounded Nightshift fixture to test policies, but do not call Nightshift governed until the enforcement path is implemented and checked.

**Next human effort:** Freeze acceptance criteria and review adversarial labels, mutation behavior and false positives.

**Bounded Nightshift work:** Build a corpus harness and regression fixtures for malformed judge output, changed content after approval and symlink cases.

**Promote / stop gate (proposed):** Require deterministic integrity cases to pass and report semantic misses and false positives separately. A reproducible bypass blocks a security-readiness claim; it is a useful research result.


## TSLIT-DSPy DGX

**Current state:** Evidence-selected experimental flagship; negative and withdrawn results preserved.

**Market boundary:** Controlled model-integrity experiments for researchers investigating identity/date-conditioned behavior.

**Confidence:** Low: small evaluation and weak detector evidence.

**Rivalry — 4/5 (High).** Garak and Promptfoo provide broad vulnerability/evaluation tooling. TSLIT’s opportunity is a rigorous narrow experiment, not broader scanner coverage.

**Supplier power — 4/5 (High).** Model releases, inference configuration and an independent detector determine reproducibility. Limited positive ground truth makes evaluation data a scarce input.

**Buyer power — 4/5 (High).** Researchers can run their own probes and require strong controls before relying on a detector. An all-negative holdout does not demonstrate sensitivity.

**Threat of entrants — 3/5 (Moderate).** Prompt variants are easy to create; carefully matched controls, frozen traces and independent reproduction are more difficult and more valuable.

**Threat of substitutes — 4/5 (High).** General vulnerability probes, manual paired analysis and provenance review address adjacent integrity concerns, often without a dedicated system.

**Grounding:** [NVIDIA garak](https://github.com/NVIDIA/garak), [Promptfoo](https://github.com/promptfoo/promptfoo), [TSLIT-DSPy DGX repository](https://github.com/sw30labs/tslit-dspy-dgx). Ratings and competitive implications above are analyst inferences from these sources.

**Defensible direction to test:** A falsifiable, carefully controlled study of a specific conditional behavior.

**Standalone decision:** One replication before extending detection claims.

**Holistic amendment:** Move to a rotating evidence slot. A shared evidence format with Guardrails is useful, but combining outputs must not launder weak detection into a stronger security claim.

**Next human effort:** Review the short cert_expiry cell and matched controls; distinguish truncation from a repeatable behavioral effect.

**Bounded Nightshift work:** Run frozen matched conditions with repeated seeds; retain raw outputs and configuration without rewriting holdouts.

**Promote / stop gate (proposed):** If the anomaly does not reproduce, publish a negative finding and stop expansion. If it does, require independent confirmation before describing a trigger.


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


## Singularity Atlas

**Current state:** Featured working dashboard; practical value provisional.

**Market boundary:** AI infrastructure and convergence monitoring for independent researchers and technical writers.

**Confidence:** Low: dashboard exists; decision value unmeasured.

**Rivalry — 4/5 (High).** Epoch publishes AI models, data-center and company datasets. Atlas competes for attention with specialist research feeds; a globe and composite index alone do not establish added decision value.

**Supplier power — 4/5 (High).** Upstream public feeds control availability, definitions and revisions. Open access does not imply permanent availability or unrestricted redistribution.

**Buyer power — 5/5 (Very high).** Readers can follow primary sources directly. Their switching costs are low and evidence of recurring outside use or willingness to pay was not found in the inspected material.

**Threat of entrants — 5/5 (Very high).** Feed aggregation and brief generation are accessible capabilities. A differentiated curated dataset and documented corrections would be stronger barriers.

**Threat of substitutes — 5/5 (Very high).** RSS, newsletters, bookmarks and direct dataset queries provide situational awareness without running another service.

**Grounding:** [Epoch AI datasets](https://epoch.ai/data), [Singularity Atlas repository](https://github.com/sw30labs/singularity-atlas). Ratings and competitive implications above are analyst inferences from these sources.

**Defensible direction to test:** A provenance-linked brief that changes a concrete research or writing decision.

**Standalone decision:** Keep the working dashboard; verify the value of its synthesis.

**Holistic amendment:** Use as the lab’s bounded intelligence input and distribution aid. Cap dashboard development; distinguish its editorial index from a calibrated forecast.

**Next human effort:** For one week, record which sourced signals change a project decision or produce a useful article angle.

**Bounded Nightshift work:** Check feed freshness, broken sources and duplicate stories; draft a short brief with source links for human review.

**Promote / stop gate (proposed):** Retain weekly maintenance only if useful signals outweigh reading and upkeep time; otherwise use a simpler feed list.


## VideoCortex

**Current state:** Featured PoC; local TRIBE v2 research instrument.

**Market boundary:** Local stimulus-to-predicted-brain-response tooling for neuroscience exploration and teaching.

**Confidence:** Medium for dependency and scope; low for practical demand.

**Rivalry — 3/5 (Moderate).** The upstream TRIBE v2 notebook and demo already offer the underlying scientific capability. Local preflight, platform support and clearer figures are the instrument’s value.

**Supplier power — 5/5 (Very high).** TRIBE v2 is the central model dependency and its repository specifies CC-BY-NC-4.0. That materially constrains assuming a straightforward commercial offering; replacing the core would be costly.

**Buyer power — 4/5 (High).** Researchers can use the upstream notebook and demand validity for their study. Attractive cortical plots are insufficient evidence of practical or personalized accuracy.

**Threat of entrants — 4/5 (High).** A visual wrapper is relatively accessible; numerical parity, timing correctness and trustworthy cross-device behavior require more careful work.

**Threat of substitutes — 4/5 (High).** Upstream notebooks, generic cortical visualization and simpler stimulus analysis can address teaching or exploratory needs without this package.

**Grounding:** [Meta TRIBE v2 and license](https://github.com/facebookresearch/tribev2), [VideoCortex repository](https://github.com/sw30labs/videocortex). Ratings and competitive implications above are analyst inferences from these sources.

**Defensible direction to test:** A reproducible local instrument with explicit average-subject limits and verified output parity.

**Standalone decision:** Explore practical value through a narrowly defined research use case.

**Holistic amendment:** Keep as a research/teaching option and rotate only for a parity or user-validation experiment. Do not frame it as generic video understanding or individualized neuroscience.

**Next human effort:** Choose one research/teaching task and review real versus synthetic output and licensing dependencies.

**Bounded Nightshift work:** Prepare a pinned reference fixture and compare supported backends within an explicitly chosen numerical tolerance.

**Promote / stop gate (proposed):** No promotion beyond PoC until a real use case and upstream parity are demonstrated. Commercial prioritization requires resolving applicable permissions first.


## AI-OS-1

**Current state:** Featured design corpus; no runtime.

**Market boundary:** Model-aware scheduling and placement for bandwidth-constrained local multi-node inference.

**Confidence:** Low: design only; no performance advantage established.

**Rivalry — 5/5 (Very high).** DwarfStar supplies the native engine and vLLM already documents multi-node parallelism. An OS-sized design must beat a simple engine configuration on a specified workload to justify itself.

**Supplier power — 5/5 (Very high).** The hardware interconnect, engine interfaces and model architecture tightly constrain implementation. Supporting all three creates concentrated technical dependency.

**Buyer power — 4/5 (High).** Local operators can keep a model on one box or use established engines. They need measured latency, throughput and capacity improvements before adopting another control layer.

**Threat of entrants — 3/5 (Moderate).** A robust scheduler has meaningful engineering barriers, but capable engine maintainers can incorporate useful optimizations. A design document alone does not create that barrier.

**Threat of substitutes — 5/5 (Very high).** Single-node serving, static placement and existing tensor/pipeline parallelism can eliminate the need for a new system layer.

**Grounding:** [vLLM parallelism and scaling](https://docs.vllm.ai/en/latest/serving/parallelism_scaling/), [DwarfStar inference engine](https://github.com/antirez/ds4), [AI-OS-1 repository](https://github.com/sw30labs/AI-OS-1). Ratings and competitive implications above are analyst inferences from these sources.

**Defensible direction to test:** One independently reproducible placement improvement on existing Sparks, with end-to-end benefit.

**Standalone decision:** Run Phase 0 before writing the runtime.

**Holistic amendment:** Make this an infrastructure option. Promote only if measurements identify a bottleneck that also materially limits useful Nightshift work; avoid a hardware rewrite driven by theoretical elegance.

**Next human effort:** Approve a fixed workload, single-node baseline and decision threshold before a placement comparison.

**Bounded Nightshift work:** Prepare reproducible measurement scripts and manifests; reserve hardware measurements for an exclusive slot, separate from overnight coding.

**Promote / stop gate (proposed):** If an existing engine configuration meets the workload need, stop at the evidence report. A proposed 20% useful-work improvement is a planning threshold to agree before testing, not an achieved result.


## AEGIS

**Current state:** Featured research proposal; no implementation or measured performance.

**Market boundary:** Locally operated, governed security assessment for teams needing reproducible scoped workflows.

**Confidence:** Low: proposal; market demand unvalidated.

**Rivalry — 5/5 (Very high).** Pentera addresses automated security validation; existing security tools and service providers bring experience and trust. A new appliance must demonstrate a specific unmet workflow.

**Supplier power — 4/5 (High).** Hardware, local models and tool integrations create several maintenance dependencies. Specialized hardware would add servicing and supply constraints before demand is established.

**Buyer power — 5/5 (Very high).** Security teams can choose existing services and require auditable scope control. Procurement and trust requirements create substantial adoption friction for an unimplemented proposal.

**Threat of entrants — 3/5 (Moderate).** Prototypes are accessible; dependable enforcement, recovery and service support are much harder. These barriers burden AEGIS now rather than protect it.

**Threat of substitutes — 5/5 (Very high).** A commodity workstation, existing assessment tools and a human-reviewed playbook may meet the same need with less integration risk.

**Grounding:** [Pentera security validation solution brief](https://pentera.io/wp-content/uploads/2026/04/security_validation_for_the_financial_industry.pdf), [Cisco Skill Scanner](https://github.com/cisco-ai-defense/skill-scanner), [AEGIS repository](https://github.com/sw30labs/aegis-research). Ratings and competitive implications above are analyst inferences from these sources.

**Defensible direction to test:** A small software reference proving scope enforcement and evidence capture on an authorized synthetic target.

**Standalone decision:** Start a software reference on existing hardware.

**Holistic amendment:** Defer active build until a concrete user workflow is validated. Reuse Guardrails findings, but do not assume admission control proves tool mediation or that named research connections are integrations.

**Next human effort:** Validate one operator need and specify a minimal authorized target and forbidden actions.

**Bounded Nightshift work:** Only after that gate: prepare synthetic fixtures and testable enforcement acceptance cases.

**Promote / stop gate (proposed):** No appliance/custom-silicon work before the reference demonstrates value beyond existing tools and the operator need is confirmed.


## RPC-H16

**Current state:** Frontier flagship; initial software experiment, physical concept unproven.

**Market boundary:** Early fault-tolerant optical architecture research; future adopter segment remains hypothetical.

**Confidence:** Very low commercial confidence; early software evidence only.

**Rivalry — 4/5 (High).** Photonic interconnect suppliers such as Lightmatter illustrate a developed adjacent ecosystem, not direct validation or competition for the same H16 logic. Research groups and conventional architectures compete for attention and future application fit.

**Supplier power — 5/5 (Very high).** A physical path would depend on optical components, alignment, detectors and fabrication access. The present software experiment has much lower supplier exposure than a future device.

**Buyer power — 5/5 (Very high).** Any future integrator would require end-to-end reliability, energy and useful-computation evidence. No validated buyer segment or procurement path is established.

**Threat of entrants — 2/5 (Moderate-low).** Physical optical systems have high entry barriers, hence relatively low entrant threat. Those same barriers make commercialization difficult for a solo lab; they are not evidence of a moat here.

**Threat of substitutes — 5/5 (Very high).** Electronic fault tolerance, conventional routing and simpler redundant systems set the baseline. Optical transport alone does not demonstrate a superior computing system.

**Grounding:** [Lightmatter photonic interconnect platform](https://lightmatter.co/products/passage), [RPC-H16 repository](https://github.com/sw30labs/.github/blob/main/research/flagships.md#frontier-flagship-rpc-h16). Ratings and competitive implications above are analyst inferences from these sources.

**Defensible direction to test:** A small falsifiable result about physically feasible channel mappings and failure behavior.

**Standalone decision:** Protect a bounded frontier experiment despite weak near-term commercial attractiveness.

**Holistic amendment:** Preserve a 10% curiosity allocation instead of ranking it as a near-term product. Separate software evidence from physical feasibility; do not use high hardware barriers as a reason to overinvest.

**Next human effort:** Specify physical node bodies, line-of-sight/clearance rules and channel mapping for E002; interpret the result.

**Bounded Nightshift work:** Create deterministic geometry fixtures and a reproducible report once the human approves assumptions; no model in the numerical decision path.

**Promote / stop gate (proposed):** After one bounded E002 cycle, record feasible/infeasible under stated assumptions. Stop geometry expansion if the model adds complexity without discriminating among designs.


## Evidence notes and limitations

The live SW30 dossiers record TSLIT’s synthetic detector accuracy as 0.4117647 on 17 cases; its ten-case all-negative holdout cannot establish attack sensitivity. They also record Wiki vs RAG’s 30 cases per strategy: agentic RAG used fewer tokens than wiki navigation but had higher mean latency. Neither supports a universal detector or retrieval winner. These are inspected historical artifacts, not fresh executions. [SW30 evidence dossiers](https://github.com/sw30labs/.github/blob/main/research/flagships.md).

RPC-H16 has an initial software propagation experiment; optical hardware and system-wide benefit remain unproven. Only the public research scope is included here, with no private simulator source or raw experimental dataset.

TRIBE v2 explicitly identifies average-subject predictions and CC-BY-NC-4.0 licensing. That is a source-stated dependency constraint, not a legal opinion about every possible VideoCortex use. [Upstream repository](https://github.com/facebookresearch/tribev2).

External vendor materials establish what vendors describe or offer, not independent comparative performance. No market sizes, revenues, adoption counts, energy savings or financial forecasts are invented. AEGIS’s buyer-power rating and RPC-H16’s industry ratings are especially provisional because the proposed offerings are not validated products.
