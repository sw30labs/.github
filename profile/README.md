# SW3.0 Labs

<table>
  <tr>
    <td width="76" valign="middle">
      <a href="https://github.com/sw30labs/.github/wiki">
        <img src="https://github.com/sw30labs/.github/blob/main/wiki-icon.png?raw=true" width="64" alt="SW3.0 Labs wiki" />
      </a>
    </td>
    <td valign="middle">
      <strong><a href="https://github.com/sw30labs/.github/wiki">SW3.0 Labs Wiki</a></strong><br />
      Catalog of every live repo. GitHub hides the wiki tab; this is the front door.<br />
      <a href="https://github.com/sw30labs/.github/wiki/tslit">TSLIT</a>
      &nbsp;·&nbsp;
      <a href="https://github.com/sw30labs/.github/wiki/singularity-atlas">The Singularity Atlas</a>
      &nbsp;·&nbsp;
      <a href="https://github.com/sw30labs/.github/wiki/oscal-compliance">OSCAL</a>
    </td>
  </tr>
</table>

**Building the inference layer as the primary enterprise operating layer.**

<p align="center">
  <img src="https://github.com/sw30labs/.github/blob/main/sw30evolution.png?raw=true" alt="SW 3.0 Labs" />
</p>

*"We build open-source tools at the intersection of AI agents, cybersecurity, and local inference — with a bias toward production-grade security, Apple Silicon optimization, and agentic automation."*

<!-- wiki-home:start -->
<!-- AUTO-GENERATED from the org wiki Home page by .github/workflows/sync-profile-readme.yml.
     Edit https://github.com/sw30labs/.github/wiki/Home — changes here will be overwritten. -->

---

**Author:** Nicolas Cravino | **Repos:** 40 live *(25 archived repos are not tracked)* | **Articles:** 34 | **Last updated:** 2026-08-30

---

### 🔒 AI Security & Pentesting

LLM integrity testing, regulatory intelligence for global pentest compliance, autonomous pentesting research, and enterprise AI-assisted pentesting specifications.

| Repository | Description |
|---|---|
| [tslit-dspy-dgx](https://github.com/sw30labs/tslit-dspy-dgx) | TSLIT — time-shift integrity testing on DGX Spark (Ollama, Muse-light detective; Qwen is a scan target, never the detector). Lineage: [tslit](https://github.com/sw30labs/.github/wiki/tslit) |
| [pentest-regulatory-intel](https://github.com/sw30labs/pentest-regulatory-intel) | RegIntel — AI-powered pentest regulation inventory across 20+ jurisdictions with reflection quality gates |
| [strixresearch](https://github.com/sw30labs/strix-research) | Research and documentation for the Strix autonomous AI pentesting platform |
| [agentic-ai-pentesting](https://github.com/sw30labs/agentic-ai-pentesting) | Book companion — two approaches to AI-assisted pentesting (autonomous platform + Burp Suite co-pilot) |
| [skillspector-trial](https://github.com/sw30labs/skillspector-trial) | Skillspector — single-file offline scanner grading Agent Skills A–F on security + quality, now with an optional loopback oMLX "AI Analyst" that triages, adjudicates, and issues an install verdict (static evidence stream for oscal-skills-guardrails) |
| [strix-omlx](https://github.com/sw30labs/strix-omlx) | Points the Strix autonomous pentest agent at a local OMLX MLX server (abliterated MiniMax-M2) — fully local, LiteLLM routing; companion to strixresearch |
| [STRIDE-Lite](https://github.com/sw30labs/STRIDE-Lite) | Local STRIDE/DREAD threat models, ATT&CK-templated kill-chain scenarios, and a linked-note Vault with a phase × lane Campaign Score — LangGraph, OpenAI-compatible or local oMLX |
| [LangGraph_STRIDE](https://github.com/sw30labs/LangGraph_STRIDE) | Dual-platform LangGraph STRIDE/DREAD threat models plus CVE/CTI/scenario graphs — same codebase on DGX Spark (vLLM) and Apple Silicon (oMLX); Maintain studio + optional Neo4j |

**Category page:** [ai-security-pentesting](https://github.com/sw30labs/.github/wiki/ai-security-pentesting) · **TSLIT lineage:** [tslit](https://github.com/sw30labs/.github/wiki/tslit)

---

### 🛡️ OSCAL & Compliance

NIST OSCAL-powered tools for agent guardrails, digital twin compliance, Zero Trust posture analysis, and compliance-as-code workflows.

| Repository | Description |
|---|---|
| [oscal-agent-guardrails](https://github.com/sw30labs/oscal-agent-guardrails) | OSCAL profiles as a policy brain to guardrail LLM agents at runtime (allow/deny/needs_approval) |
| [oscal-digital-twin-playground](https://github.com/sw30labs/oscal-digital-twin-playground) | Digital twin drift detection — SSP vs live config, with risk assessment and mitigation |
| [oscal-zero-trust-lens](https://github.com/sw30labs/oscal-zero-trust-lens) | Zero Trust coverage analysis across 7 dimensions from SP 800-53 controls |
| [oscal-agent-lab](https://github.com/sw30labs/oscal-agent-lab) | Multi-agent lab — RAG Q&A, SSP diff, profile generation, validation over 1,196 controls |
| [oscal-cac-playgd](https://github.com/sw30labs/oscal-cac-playgd) | Compliance-as-code CLI — explain OSCAL files, suggest remediation, PR-style diff review |
| [genai-regulatory-intel](https://github.com/sw30labs/genai-regulatory-intel) | RegIntel-AgenticAI — autonomous GenAI regulatory intelligence across 16 global financial jurisdictions (LangGraph 4-agent state machine) |
| [oscal-skills-guardrails](https://github.com/sw30labs/oscal-skills-guardrails) | OSCAL-as-policy for Agent Skills — dual-evidence admission (static scan + local LLM rubric judge), digest integrity, CI gate, assessment-results audit trail |
| [driftlab-mlx](https://github.com/sw30labs/driftlab-mlx) | Runtime compliance observer — diffs a live agent's decision traces against a certified OSCAL baseline, proves drift via sandboxed micro-experiments, emits OSCAL 1.1.2 assessment-results (CA-7); v2.1 adds DL-8 certified resource budgets (renamed from driftlab) |
| [driftlab-dgx](https://github.com/sw30labs/driftlab-dgx) | DriftLab on NVIDIA DGX Spark — same 2.1.0 core and deterministic compliance path, advisory layer on the host's shared local vLLM stack |
| [oscal-presence-gate](https://github.com/sw30labs/oscal-presence-gate) | OSCAL as the policy brain for WHERE, not just WHAT — presence verifier ahead of the enforcer for delegated agent traffic (EO 14117 / DOJ DSP); unknown presence fails closed; first public OSCAL encoding of the CISA Security Requirements + 5-control PRES overlay |

**Category page:** [oscal-compliance](https://github.com/sw30labs/.github/wiki/oscal-compliance)

---

### 🤖 Agentic Frameworks

Design patterns, orchestration, workflow conversion, coding assistants, and research automation using LangGraph.

| Repository | Description |
|---|---|
| [agent-stack](https://github.com/sw30labs/agent-stack) | Interactive 10-layer architecture visualization for reliable AI agents (vis.js) |
| [deepagent-azure-cli](https://github.com/sw30labs/deepagent-azure-cli) | Turnkey coding assistant CLI — Azure OpenAI + LangChain DeepAgents, Textual TUI, HITL |
| [ralph-dgx](https://github.com/sw30labs/ralph-dgx) | DeepAgents Code CLI + Ralph goal loop on DGX Spark — install→patch→overlay harness against local vLLM (Qwen3-Coder-Next-FP8) |
| [wiki-vs-rag](https://github.com/sw30labs/wiki-vs-rag) | Four-arm benchmark over the sw30labs wiki — single-shot RAG vs agentic-RAG vs wiki-nav vs QMD; agentic-RAG wins Pareto |
| [langgraph-checkpoints-vs-stores](https://github.com/sw30labs/langgraph-checkpoints-vs-stores) | Runnable offline reference — thread-scoped checkpoints vs cross-thread stores, real StateGraph/InMemorySaver/InMemoryStore, CI-gated; production backends (SQLite/Postgres/Redis) + HITL/time-travel chapters |
| [loopscope](https://github.com/sw30labs/loopscope) | Local live dashboard for LangGraph graphs and Ralph loops — in-process hook, :7788, ring buffer over a websocket, JSONL record/replay; forget the hook and the agent still runs |
| [singularity-atlas](https://github.com/sw30labs/singularity-atlas) | The Singularity Atlas — fuses public AI-buildout feeds into a globe, eight vector panels, a 0–100 Singularity Index and a locally-written daily brief (LangGraph → Neo4j, optional Ollama) |

**Category page:** [agentic-frameworks](https://github.com/sw30labs/.github/wiki/agentic-frameworks) · **Atlas:** [singularity-atlas](https://github.com/sw30labs/.github/wiki/singularity-atlas)

---

### 🍎 Local Inference & MLX

On-device AI toolkit for Apple Silicon — inference serving, benchmarking, distillation, vision-language, TTS, STT.

| Repository | Description |
|---|---|
| [tars-ai](https://github.com/sw30labs/tars-ai) | TARS from Interstellar as a local voice agent — LLM + TTS served by a local OMLX server (OpenAI protocol), zero cloud; LangGraph dropped July 2026 for a plain orchestrator, now with a multi-character crew and a TUI |
| [screen-lens-mlx](https://github.com/sw30labs/screen-lens-mlx) | Video scene intelligence — hybrid keyframe detection, local VLM captioning, ChromaDB search, code/docs/demo reconstruction. Re-converged to dual-platform in Aug 2026: one client over vLLM/CUDA *or* oMLX/MPS, split vision/text model roles, web command deck |
| [mlx-distillation-explained](https://github.com/sw30labs/mlx-distillation-explained) | Educational distillation PoC — Claude Sonnet → Llama 3.1 8B via LoRA on Apple Silicon |
| [mlx-responses-api-server](https://github.com/sw30labs/mlx-responses-api-server) | OpenAI/Azure/Anthropic-compatible local inference server with tool calling (renamed from local-mlx-responsesAPI-server) |
| [QWEN3-VL-Python-OCR-Script-MLX](https://github.com/sw30labs/QWEN3-VL-Python-OCR-Script-MLX) | Batch image captioning with Qwen3-VL-30B on MLX |
| [MLX-YouTubeScribe](https://github.com/sw30labs/MLX-YouTubeScribe) | YouTube transcription using local Whisper models with Streamlit UI |
| [sulphur-2-base](https://github.com/sw30labs/sulphur-2-base) | Local MLX video generation wrapper for Sulphur 2 via ltx-2-mlx runtime |
| [supertonic-3-mlx](https://github.com/sw30labs/supertonic-3-mlx) | Local MLX TTS for Supertonic 3 — JSON graph topology + NPZ weights |

**Category page:** [local-inference-mlx](https://github.com/sw30labs/.github/wiki/local-inference-mlx)

---

### ⚡ Local Inference & DGX Spark

CUDA counterpart to the MLX toolkit — local inference on NVIDIA DGX Spark (GB10, Linux aarch64) via local vLLM and CUDA llama.cpp.

| Repository | Description |
|---|---|
| [screen-lens-dgx](https://github.com/sw30labs/screen-lens-dgx) | DGX-only ScreenLens fork — vLLM (Qwen3.6-27B-FP8) captioning, OpenCLIP on CUDA, ChromaDB, Docker compose path |
| [AI-OS-1](https://github.com/sw30labs/AI-OS-1) | Research corpus (no runtime) for a model-aware distributed inference OS on N ≥ 2 DGX Sparks — paper, frozen schemas, append-only design forum |

**Category page:** [local-inference-dgx](https://github.com/sw30labs/.github/wiki/local-inference-dgx)

---

### 🔧 Developer Tools

CLI utilities, code intelligence, and infrastructure for managing repository fleets.

| Repository | Description |
|---|---|
| [gitnexus_fleet](https://github.com/sw30labs/gitnexus_fleet) | Clone, index (KuzuDB graph), and query entire GitHub orgs via MCP + web dashboard |
| [RepoBundle](https://github.com/sw30labs/RepoBundle) | Export/import Git repos as single human-readable text files |
| [cleanroom](https://github.com/sw30labs/cleanroom) | Agentic file-hygiene pipeline — Analyze → Recommend → Remediate → QA over one file via LangGraph, oMLX or DGX vLLM, honest about what it can and can't verify |

**Category page:** [developer-tools](https://github.com/sw30labs/.github/wiki/developer-tools)

---

### Miscellaneous Research

One-off research instruments that do not sit in security, OSCAL, agents, or local inference. Two encoding instruments: Mac and Spark.

| Repository | Description |
|---|---|
| [videocortex](https://github.com/sw30labs/videocortex) | Drop a clip. See which cortical regions TRIBE v2's average subject would fire. Encoding, not decoding — local instrument around Meta TRIBE v2 (Metal, preflight, plates) |
| [videocortex-spark](https://github.com/sw30labs/videocortex-spark) | Same instrument on NVIDIA DGX Spark (GB10 / CUDA 13). UMA from meminfo, CIRC-fixed runs view, plus `export` / `sonify` |

**Category page:** [miscellaneous-research](https://github.com/sw30labs/.github/wiki/miscellaneous-research)

---

### 📰 Published Articles

Long-form companion writing to the repos above — 34 articles spanning
2023-04 to 2026-07, covering AI security governance, agentic pentesting,
OSCAL-as-code, custom silicon economics, and zero-trust AI coding.

See [timeline](https://github.com/sw30labs/.github/wiki/timeline) for the chronological list, or [Index](https://github.com/sw30labs/.github/wiki/Index) for all article
pages grouped by category. Articles are also linked from each category
page under the "Related Articles" heading.

---

### 🧩 Cross-cutting patterns

Across all 45 live repositories, several architectural patterns recur
(counts from the `stacks:` frontmatter of repo stubs, see [Sitemap-Stacks](https://github.com/sw30labs/.github/wiki/Sitemap-Stacks)):

- **Agentic** — multi-agent orchestration / tool-using agents (24 repos)
- **LangGraph / LangChain** — dominant orchestration framework (24 repos)
- **Apple MLX** — on-device inference on Apple Silicon (16 repos)
- **CLI / Tooling** — command-line utilities and workflow glue (13 repos)
- **Compliance** — regulatory frameworks, controls mapping (12 repos)
- **OSCAL** — NIST OSCAL data model (SSPs, profiles, controls) (9 repos)
- **Pentest** — offensive security, red-teaming, vulnerability discovery (8 repos)
- **NVIDIA DGX Spark** — CUDA / local vLLM ports of the desk fleet (8 repos)
- **RAG** — retrieval-augmented generation, vector stores (5 repos)
- **Converter** — file-format conversion, OCR, doc-to-markdown (3 repos)
- **MCP** — Model Context Protocol servers / tooling (2 repos)
- **Pydantic** for data validation (nearly universal)
- **Typer + Rich** or **Click + Rich** for CLI interfaces
- **Karpathy LLM Wiki pattern** for knowledge bases (this wiki)
- **Dual-platform siblings** — Apple Silicon and DGX Spark trees of the same product: driftlab, screen-lens (mlx/oMLX vs vLLM), videocortex (Metal vs CUDA). TSLIT collapsed to one live spine ([tslit](https://github.com/sw30labs/.github/wiki/tslit)); there is no public mlx TSLIT-DSPy repo.

---

*Wiki structure: see [SCHEMA](https://github.com/sw30labs/.github/wiki/SCHEMA) | Full index: [Index](https://github.com/sw30labs/.github/wiki/Index) | Visual map: [Sitemap](https://github.com/sw30labs/.github/wiki/Sitemap) | Change log: [Log](https://github.com/sw30labs/.github/wiki/Log) | Stacks view: [Sitemap-Stacks](https://github.com/sw30labs/.github/wiki/Sitemap-Stacks)*

*<sub>This section is mirrored automatically from the [org wiki](https://github.com/sw30labs/.github/wiki) — edit the wiki, not this file.</sub>*
<!-- wiki-home:end -->

---

### 📖 Books

<a href="https://a.co/d/07Fndacy">
  <img src="https://github.com/sw30labs/.github/blob/main/book1cover.png" width="150" alt="AI Agents in Cybersecurity" align="left" />
</a>

**Author.** **AI Agents in Cybersecurity** — A Practitioner's Guide, from Strategy to Implementation.

How autonomous agents are transforming enterprise security — from automating SOC operations and incident triage to building multi-agent defense systems. Includes real-world case studies, practical frameworks, and a hands-on lab companion.

[![Apple Books](https://img.shields.io/badge/Apple_Books-000000?style=for-the-badge&logo=apple&logoColor=white)](https://books.apple.com/us/book/ai-agents-in-cybersecurity/id6751737181)
[![Amazon](https://img.shields.io/badge/Amazon-FF9900?style=for-the-badge&logo=amazon&logoColor=white)](https://a.co/d/07Fndacy)
[![GitHub](https://img.shields.io/badge/Companion_Code-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ai-agents-cybersecurity/complete)

<br clear="left" />

<a href="https://www.amazon.com/dp/B0GX31SFJJ">
  <img src="https://github.com/sw30labs/.github/blob/main/book2cover.png" width="150" alt="The Human-Agent Orchestrator" align="left" />
</a>

**Named key contributor.** **The Human-Agent Orchestrator** — Leading and Scaling AI-Driven Organizations.

Pascal Bornet, Jochen Wirtz, et al. System contribution: designed/implemented customer-facing workflows for a related orchestration design canvas and workshop ecosystem.

[![Apple Books](https://img.shields.io/badge/Apple_Books-000000?style=for-the-badge&logo=apple&logoColor=white)](https://books.apple.com/us/book/the-human-agent-orchestrator-leading-and-scaling/id6771782989)
[![Amazon](https://img.shields.io/badge/Amazon-FF9900?style=for-the-badge&logo=amazon&logoColor=white)](https://www.amazon.com/dp/B0GX31SFJJ)

<br clear="left" />

<a href="https://www.amazon.com/dp/B0F1DS36YC">
  <img src="https://github.com/sw30labs/.github/blob/main/book3cover.png" width="150" alt="Agentic Artificial Intelligence" align="left" />
</a>

**Named key contributor.** **Agentic Artificial Intelligence** — Harnessing AI Agents to Reinvent Business, Work and Life.

Pascal Bornet, Jochen Wirtz, Thomas H. Davenport, et al. Named key contributor on this practitioner guide (Forbes 2025 must-read).

[![Apple Books](https://img.shields.io/badge/Apple_Books-000000?style=for-the-badge&logo=apple&logoColor=white)](https://books.apple.com/us/book/agentic-artificial-intelligence/id6744370588)
[![Amazon](https://img.shields.io/badge/Amazon-FF9900?style=for-the-badge&logo=amazon&logoColor=white)](https://www.amazon.com/dp/B0F1DS36YC)

<br clear="left" />

---

*Built by [Nic Cravino](https://github.com/ai-agents-cybersecurity) · AI/ML Engineering · Cybersecurity · Enterprise Automation*
