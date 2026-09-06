# Flagship research — evidence and next tests

The initial three existing flagships are selected for inspectable implementation or experiment records. Selection is editorial, not a certificate of scientific validity. This pass read repository artifacts; it did not rerun hosted inference, hardware benchmarks, or the full source test suites.

## OSCAL Skills Guardrails

**Question:** Can policy-driven admission combine static and semantic evidence while detecting later skill mutation?

**Status:** reference implementation with test sources and an explicit hardening roadmap.

**Architecture:** skill files → static scan + local rubric judge → OSCAL policy → admission/runtime gates → assessment-results.

**Evidence:** [rubric-judge tests](https://github.com/sw30labs/oscal-skills-guardrails/blob/9d848f0c79f2b91305c86e8539a5cd016a90b273/tests/test_rubric_judge.py), [digest tests](https://github.com/sw30labs/oscal-skills-guardrails/blob/9d848f0c79f2b91305c86e8539a5cd016a90b273/tests/test_digest_verification.py), and [roadmap](https://github.com/sw30labs/oscal-skills-guardrails/blob/9d848f0c79f2b91305c86e8539a5cd016a90b273/ROADMAP.md). The README's passing-test badge is a repository claim, not a fresh run here.

**Limitations that matter:** the roadmap calls for digest-bound approvals, subagent digest coverage, consistent symlink policy, strict OSCAL validation, and a golden semantic-judge evaluation. “Static 100/A, semantic deny” is an illustrative case, not a population-level recall estimate. Do not repeat broad “TOCTOU closed” or “never fails open” claims as established across every execution context.

**Next experiment (proposed OSG-E001):** freeze a clean/adversarial skill corpus and judge configuration; compare static-only and combined admission, including false positives, missed cases, malformed judge output and changed content after approval. Predeclare criteria; preserve per-case evidence and environment.

## TSLIT-DSPy DGX

**Question:** Does model behavior change across controlled identity/date conditions, and can an independent detector distinguish suspicious changes from ordinary variation?

**Status:** experimental corpus with live traces, synthetic tests, and explicit withdrawn work.

**Architecture:** controlled target probes → paired/triaged responses → separate detector → evidence-labeled analysis. Target and detector are distinct roles.

**Evidence:** [current paper](https://github.com/sw30labs/tslit-dspy-dgx/blob/9010df07670c1abb17175d7764a77ee06707fbae/docs/PAPER.md), [frozen synthetic-test record](https://github.com/sw30labs/tslit-dspy-dgx/blob/9010df07670c1abb17175d7764a77ee06707fbae/workspace/evaluation/compare/muse_light_test.json), [live-holdout record](https://github.com/sw30labs/tslit-dspy-dgx/blob/9010df07670c1abb17175d7764a77ee06707fbae/workspace/evaluation/compare/muse_light_live_holdout.json).

**Observed artifact values:** the inspected Muse-light synthetic test reports accuracy **0.4117647** on **17** cases, including zero recall for affiliation_bias. The live holdout reports ten `none` cases correctly labeled. That all-negative holdout cannot establish sensitivity to actual attacks. The paper reports 70/70 English `none` under thinking-off/tools-none conditions; this is not proof that the target has no trigger. The earlier 88.2% belongs to a different detector on planted examples.

**Failure is a result:** the paper explicitly withdraws the old autoresearch phases. Preserve that finding rather than selling the withdrawn loop as present infrastructure.

**Next experiment (proposed TSLIT-R01):** reproduce the anomalously short `cert_expiry` cell with matched siblings and repeated runs; distinguish truncation from a stable effect. Keep English, language×identity, thinking-on and tools-on studies separate. Do not silently alter the frozen holdout.

## Wiki vs RAG

**Question:** What quality, token and latency tradeoffs arise from four retrieval strategies on the same corpus?

**Status:** recorded comparative experiment; external validity and independent reproduction remain open.

**Architecture:** shared wiki corpus/questions → single-shot RAG, agentic RAG, wiki navigation, QMD → common judge → recorded analysis.

**Evidence:** [summary](https://github.com/sw30labs/wiki-vs-rag/blob/463886eb5993fcbd9a4bca43c98292f357f24a5d/report/summary.json), [per-run results](https://github.com/sw30labs/wiki-vs-rag/blob/463886eb5993fcbd9a4bca43c98292f357f24a5d/report/results.csv), [run metadata](https://github.com/sw30labs/wiki-vs-rag/blob/463886eb5993fcbd9a4bca43c98292f357f24a5d/runs/run_summary.json).

| Recorded strategy | Cases | Mean judge quality | Mean tokens | Mean latency (s) |
|---|---:|---:|---:|---:|
| Single-shot RAG | 30 | 4.45 | 1,366 | 5.37 |
| Agentic RAG | 30 | 4.77 | 7,147 | 13.70 |
| Wiki navigation | 30 | 4.69 | 19,120 | 11.70 |
| QMD | 30 | 3.56 | 922 | 10.14 |

**Finding limited to these records:** agentic RAG used about 37% of wiki-navigation tokens with similar mean judged quality, but was slower on average. This is not a universal winner across quality, cost and latency. The qualitative radar scores are editorial values, not measured performance. Do not treat historical cost estimates as current prices.

**Next experiment (proposed WVR-R01):** rerun the frozen questions with repeated seeds, audit judge bias and failures, report uncertainty, then test a second corpus. Keep parsing/indexing, retrieval and generation costs distinct.

## Design spotlight: AI-OS-1

[AI-OS-1](https://github.com/sw30labs/AI-OS-1) is a model-aware distributed-inference **design corpus, not a runtime**. Its paper, frozen interfaces and [research ledger](https://github.com/sw30labs/AI-OS-1/blob/37c940c5fcc5cd4e515db5cdf45e88d350a803fb/research/ledger.md) make it a strong architecture spotlight. Implementation and claimed performance require the Phase-0 measurements specified by the project. It is ACTIVE/design-only here, rather than one of the initial empirical/reference flagships.

## Frontier flagship: RPC-H16

**Planned research:** a hexadecimal-native architecture with sixteen logical optical channels 0–F, a 3D topology, fault injection and intermittent energy. Sixteen logical channels do not prescribe sixteen physical faces. Simulation precedes physical optics. No optical prototype, energy advantage or space qualification is claimed. Its initial work is staged privately; no private repository details are exposed here.

## Loopscope

**Flagship designation:** owner decision, 2026-09-06.

**Evidence:** the owner reports daily personal use and positive user feedback. This is attributed usage evidence, not an independently measured adoption study.

**Program:** AI & Computing Systems; cross-cutting Research Engine observability.

**Maturity:** operational within the owner's workflow. Broader production readiness remains unverified.

**Next milestone:** document the daily workflow, failure/recovery behavior and one reproducible example showing how observability helps diagnose an agent run.

## Nightshift

**Research Engine flagship**, added with the 2026-09-06 portfolio assessment. Implemented bounded overnight coding workflow with frozen briefs, host checks and reviewable branches. This designation does not certify autonomous reliability or measured productivity.

**Next milestone:** track accepted work and net human time saved after briefing, review, repair and maintenance; retain failed runs in the denominator.

[Porter assessment](porter/nightshift-porter.md) · [Interactive portfolio priorities](https://sw30labs.github.io/.github/porter.html)
