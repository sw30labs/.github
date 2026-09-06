# OSCAL Skills Guardrails — Porter Five Forces

6 September 2026. Analyst assessment; 1 = low pressure, 5 = very high. Read with the portfolio report for scope, assumptions and weekly allocation.

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

