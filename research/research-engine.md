# SW30 Research Engine

Cross-cutting research infrastructure for all four programs; not a fifth program.

**Hypothesis → experiment → evidence → finding → kill / modify / reproduce / promote.**

Use deterministic tools for parsing, simulation and verification. Use the local model fleet for bulk work and bounded critique. Escalate hard synthesis to GPT-5.6 Sol and reserve scarce Astra/frontier use for a precise adversarial or principal-investigator review. These names express a routing preference; verify supported endpoints and budget before use.

Existing building blocks include [LoopScope](https://github.com/sw30labs/loopscope), [Ralph DGX](https://github.com/sw30labs/ralph-dgx), [Nightshift](https://github.com/sw30labs/nightshift), [Spark Serve](https://github.com/sw30labs/spark-serve), and [the Spark interconnect lab](https://github.com/sw30labs/dgx-spark-roce-lab). Their documentation does not establish a unified deployed Research Engine.

PAIR-style availability routing is a proposed integration. Request routing is separate from tensor parallelism and cannot be assumed to pool model memory. Verify an existing installation and official compatibility before configuration. No installation, model download or endpoint change is part of this documentation PR.

An escalation brief includes the question, assumptions, baseline, evidence, failures, competing explanations and one requested decision. Log route, model/version, reason, latency, observed cost where available, rework and decision impact. Missing usage data stays unknown. Local inference also has a cost.

A useful negative result closes a research question. A broken run needs repair and must not be reported as falsification. Store seeds, configuration, code revision, source provenance, raw outputs and interpretation separately. Start with files; build infrastructure only when repeatable work demands it.
