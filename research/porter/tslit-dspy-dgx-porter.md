# TSLIT-DSPy DGX — Porter Five Forces

6 September 2026. Analyst assessment; 1 = low pressure, 5 = very high. Read with the portfolio report for scope, assumptions and weekly allocation.

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

