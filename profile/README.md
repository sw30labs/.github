# SW3.0 Labs

<a href="https://github.com/sw30labs/.github/wiki">
  <img src="https://github.com/sw30labs/.github/blob/main/wiki-icon.png" width="40" alt="SW3.0 Labs wiki" align="right" />
</a>

**Building the inference layer as the primary enterprise operating layer.**

<p align="center">
  <img src="https://github.com/sw30labs/.github/blob/main/sw30evolution.png?raw=true" alt="SW 3.0 Labs" />
</p>

*"We build open-source tools at the intersection of AI agents, cybersecurity, and local inference — with a bias toward production-grade security, Apple Silicon optimization, and agentic automation."*

<!-- wiki-home:start -->
<!-- AUTO-GENERATED from the org wiki Home page by .github/workflows/sync-profile-readme.yml.
     Edit https://github.com/sw30labs/.github/wiki/Home — changes here will be overwritten. -->

---

**Author:** Nicolas Cravino | **Repos:** 57 | **Articles:** 34 | **Last updated:** 2026-07-29

---

### 🔒 AI Security & Pentesting

LLM integrity testing, regulatory intelligence for global pentest compliance, autonomous pentesting research, and enterprise AI-assisted pentesting specifications.

| Repository | Description |
|---|---|
| [TSLIT](https://github.com/sw30labs/TSLIT) | Time-Shift LLM Integrity Tester — detects affiliation bias and time-based logic bombs in local LLMs (3,840 interactions/model) |
| [pentest-regulatory-intel](https://github.com/sw30labs/pentest-regulatory-intel) | RegIntel — AI-powered pentest regulation inventory across 20+ jurisdictions with reflection quality gates |
| [strixresearch](https://github.com/sw30labs/strix-research) | Research and documentation for the Strix autonomous AI pentesting platform |
| [agentic-ai-pentesting](https://github.com/sw30labs/agentic-ai-pentesting) | Book companion — two approaches to AI-assisted pentesting (autonomous platform + Burp Suite co-pilot) |
| [NVD-Extractor](https://github.com/sw30labs/NVD-Extractor) | Extract critical network-attack-vector CVEs from the NVD API, filtered for Linux/Windows/external APIs |
| [skillspector-trial](https://github.com/sw30labs/skillspector-trial) | Skillspector — single-file offline scanner grading Agent Skills A–F on security + quality (the static evidence stream for oscal-skills-guardrails) |
| [strix-omlx](https://github.com/sw30labs/strix-omlx) | Points the Strix autonomous pentest agent at a local OMLX MLX server (abliterated MiniMax-M2) — fully local, LiteLLM routing; companion to strixresearch |
| [tslit-dspy-ar](https://github.com/sw30labs/tslit-dspy-ar) | TSLIT v0.2 — DSPy/MIPROv2-compiled integrity analyzer with an autoresearch self-improvement loop ("fighting AI with AI") |
| [tslit-dspy-dgx](https://github.com/sw30labs/tslit-dspy-dgx) | TSLIT-DSPy on DGX Spark — local vLLM, NVIDIA Nemotron detection brain (non-adversary models only; Qwen/DeepSeek are scan targets) |

**Category page:** [ai-security-pentesting](https://github.com/sw30labs/.github/wiki/ai-security-pentesting)

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
| [N8n2langraph](https://github.com/sw30labs/N8n2langraph) | Convert n8n workflow JSON into standalone LangGraph Python scripts |
| [sst-autoresearch](https://github.com/sw30labs/sst-autoresearch) | Speaker voice dynamics analysis via Karpathy-style autoresearch loop (Takens' embedding, Lyapunov) |
| [ralph-dgx](https://github.com/sw30labs/ralph-dgx) | DeepAgents Code CLI + Ralph goal loop on DGX Spark — install→patch→overlay harness against local vLLM (Qwen3-Coder-Next-FP8) |
| [AutogenRequirementsAgent](https://github.com/sw30labs/AutogenRequirementsAgent) | Experiment in strict JSON inter-agent messaging with nested GroupChat and local Ollama LLMs |
| [wiki-vs-rag](https://github.com/sw30labs/wiki-vs-rag) | Four-arm benchmark over the sw30labs wiki — single-shot RAG vs agentic-RAG vs wiki-nav vs QMD; agentic-RAG wins Pareto |
| [langgraph-checkpoints-vs-stores](https://github.com/sw30labs/langgraph-checkpoints-vs-stores) | Runnable offline reference — thread-scoped checkpoints vs cross-thread stores, real StateGraph/InMemorySaver/InMemoryStore, CI-gated; production backends (SQLite/Postgres/Redis) + HITL/time-travel chapters |
| [venture-pathfinder](https://github.com/sw30labs/venture-pathfinder) | Scans local repos into a Neo4j graph, then LangGraph + a Fabric-style Pattern Engine (local OMLX) surfaces recurring patterns and white-space venture paths |

**Category page:** [agentic-frameworks](https://github.com/sw30labs/.github/wiki/agentic-frameworks)

---

### 🍎 Local Inference & MLX

On-device AI toolkit for Apple Silicon — inference serving, benchmarking, distillation, vision-language, TTS, STT.

| Repository | Description |
|---|---|
| [tars-ai](https://github.com/sw30labs/tars-ai) | TARS from Interstellar as a local voice agent — LLM + TTS served by a local OMLX server (OpenAI protocol), zero cloud |
| [screen-lens-mlx](https://github.com/sw30labs/screen-lens-mlx) | Video scene intelligence — hybrid keyframe detection, Qwen3.5-VL captioning via local oMLX server, ChromaDB search, code/docs/demo reconstruction (renamed from screen-lens; DGX fork below) |
| [qwenbench-mlx](https://github.com/sw30labs/qwenbench-mlx) | Benchmark suite for Qwen 3.5 family (0.8B→35B) with auto-judge and cost-efficiency scoring |
| [mlx-distillation-explained](https://github.com/sw30labs/mlx-distillation-explained) | Educational distillation PoC — Claude Sonnet → Llama 3.1 8B via LoRA on Apple Silicon |
| [mlx-responses-api-server](https://github.com/sw30labs/mlx-responses-api-server) | OpenAI/Azure/Anthropic-compatible local inference server with tool calling (renamed from local-mlx-responsesAPI-server) |
| [audiobook_generator](https://github.com/sw30labs/audiobook_generator) | Book → audiobook conversion using Qwen3-TTS + LangGraph with QA verification |
| [QWEN3-VL-Python-OCR-Script-MLX](https://github.com/sw30labs/QWEN3-VL-Python-OCR-Script-MLX) | Batch image captioning with Qwen3-VL-30B on MLX |
| [MLX-YouTubeScribe](https://github.com/sw30labs/MLX-YouTubeScribe) | YouTube transcription using local Whisper models with Streamlit UI |
| [deepseekvl2-PDF-OCR-private](https://github.com/sw30labs/deepseekvl2-PDF-OCR-private) | Local PDF OCR using DeepSeek-VL2 MoE on NVIDIA CUDA |
| [bonsai-image-ternary-4b-mlx-2bit](https://github.com/sw30labs/bonsai-image-ternary-4b-mlx-2bit) | Local Apple Silicon wrapper for Bonsai 4B ternary-quantized image generation |
| [lance-3b-video-bf16](https://github.com/sw30labs/lance-3b-video-bf16) | Local MLX text-to-video + video Q&A (Lance 3B via lance-mlx runtime) |
| [stable-audio-3](https://github.com/sw30labs/stable-audio-3) | Stability AI audio/music generation — 433M CPU models to 1.4B CUDA, Gradio UI |
| [sulphur-2-base](https://github.com/sw30labs/sulphur-2-base) | Local MLX video generation wrapper for Sulphur 2 via ltx-2-mlx runtime |
| [supertonic-3-mlx](https://github.com/sw30labs/supertonic-3-mlx) | Local MLX TTS for Supertonic 3 — JSON graph topology + NPZ weights |
| [dflash-mlx-trial](https://github.com/sw30labs/dflash-mlx-trial) | DFlash × MLX — block-diffusion speculative decoding for Qwen3.6-27B on Apple Silicon (~3.4× faster, identical output) |
| [STTbench](https://github.com/sw30labs/STTbench) | Benchmarks speech-to-text on cost/speed/accuracy — OpenAI gpt-4o-transcribe vs local MLX Whisper, WER split into sub/del/ins |
| [ace-step-1.5-mlx](https://github.com/sw30labs/ace-step-1.5-mlx) | Local Apple Silicon text-to-song (with vocals) wrapper for ACE-Step 1.5 |
| [ltx-2.3-mlx](https://github.com/sw30labs/ltx-2.3-mlx) | Local MLX text/image/audio-to-video for Lightricks LTX 2.3 |
| [longcat-video-avatar-1.5-mlx](https://github.com/sw30labs/longcat-video-avatar-1.5-mlx) | Local MLX talking-avatar video (portrait + audio + prompt) |

**Category page:** [local-inference-mlx](https://github.com/sw30labs/.github/wiki/local-inference-mlx)

---

### ⚡ Local Inference & DGX Spark

CUDA counterpart to the MLX toolkit — local inference on NVIDIA DGX Spark (GB10, Linux aarch64) via local vLLM and CUDA llama.cpp.

| Repository | Description |
|---|---|
| [bonsai-ternary-27b-dgx](https://github.com/sw30labs/bonsai-ternary-27b-dgx) | Ternary Bonsai 27B chat stack — PrismML llama.cpp CUDA fork, llama-server (OpenAI-compatible :8080), Textual TUI with thinking stream |
| [screen-lens-dgx](https://github.com/sw30labs/screen-lens-dgx) | DGX-only ScreenLens fork — vLLM (Qwen3.6-27B-FP8) captioning, OpenCLIP on CUDA, ChromaDB, Docker compose path |

**Category page:** [local-inference-dgx](https://github.com/sw30labs/.github/wiki/local-inference-dgx)

---

### 🔧 Developer Tools

CLI utilities, code intelligence, and infrastructure for managing repository fleets.

| Repository | Description |
|---|---|
| [gitnexus_fleet](https://github.com/sw30labs/gitnexus_fleet) | Clone, index (KuzuDB graph), and query entire GitHub orgs via MCP + web dashboard |
| [AutogenDocGenerator](https://github.com/sw30labs/AutogenDocGenerator) | AutoGen-powered repo documentation generator with GroupChat agents |
| [AutogenMermaidGenerator](https://github.com/sw30labs/AutogenMermaidGenerator) | AutoGen GroupChat source code → Mermaid diagram generator |
| [OllamaPDF2Markdown](https://github.com/sw30labs/OllamaPDF2Markdown) | PDF → Markdown via Ollama multimodal models (Mistral Small 3.1 24B) |
| [RepoBundle](https://github.com/sw30labs/RepoBundle) | Export/import Git repos as single human-readable text files |
| [Word-to-Markdown-Converter](https://github.com/sw30labs/Word-to-Markdown-Converter) | .docx → Markdown converter preserving headings, lists, tables |
| [animated-GIF-Creator](https://github.com/sw30labs/animated-GIF-Creator) | Image folder or MOV → animated GIF with auto-resize |
| [nemotron-parse-spark](https://github.com/sw30labs/nemotron-parse-spark) | NVIDIA Nemotron Parse v1.2 harness for DGX Spark (Grace Blackwell GB10) — PDF → structured text + bounding boxes |

**Category page:** [developer-tools](https://github.com/sw30labs/.github/wiki/developer-tools)

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

Across all 57 repositories, several architectural patterns recur
(counts from the `stacks:` frontmatter of repo stubs, see [Sitemap-Stacks](https://github.com/sw30labs/.github/wiki/Sitemap-Stacks)):

- **LangGraph / LangChain** — dominant orchestration framework (24 repos)
- **Agentic** — multi-agent orchestration / tool-using agents (24 repos)
- **Apple MLX** — on-device inference on Apple Silicon (18 repos)
- **CLI / Tooling** — command-line utilities and workflow glue (18 repos)
- **Converter** — file-format conversion, OCR, doc-to-markdown (10 repos)
- **Compliance** — regulatory frameworks, controls mapping (11 repos)
- **Pentest** — offensive security, red-teaming, vulnerability discovery (8 repos)
- **OSCAL** — NIST OSCAL data model (SSPs, profiles, controls) (9 repos)
- **NVIDIA DGX Spark** — CUDA / local vLLM ports of the desk fleet (6 repos)
- **MCP** — Model Context Protocol servers / tooling (2 repos)
- **Pydantic** for data validation (nearly universal)
- **Typer + Rich** or **Click + Rich** for CLI interfaces
- **Karpathy LLM Wiki pattern** for knowledge bases (this wiki)
- **Dual-platform siblings** — Apple Silicon (mlx/oMLX) and DGX Spark (dgx/vLLM) trees of the same product: driftlab, screen-lens, tslit-dspy

---

*Wiki structure: see [SCHEMA](https://github.com/sw30labs/.github/wiki/SCHEMA) | Full index: [Index](https://github.com/sw30labs/.github/wiki/Index) | Visual map: [Sitemap](https://github.com/sw30labs/.github/wiki/Sitemap) | Change log: [Log](https://github.com/sw30labs/.github/wiki/Log) | Stacks view: [Sitemap-Stacks](https://github.com/sw30labs/.github/wiki/Sitemap-Stacks)*

*<sub>This section is mirrored automatically from the [org wiki](https://github.com/sw30labs/.github/wiki) — edit the wiki, not this file.</sub>*
<!-- wiki-home:end -->

---

### 📖 Book

<a href="https://a.co/d/07Fndacy">
  <img src="https://github.com/sw30labs/.github/blob/main/book1cover.png" width="150" alt="AI Agents in Cybersecurity" align="left" />
</a>

**AI Agents in Cybersecurity** — A Practitioner's Guide, from Strategy to Implementation.

How autonomous agents are transforming enterprise security — from automating SOC operations and incident triage to building multi-agent defense systems. Includes real-world case studies, practical frameworks, and a hands-on lab companion.

[![Apple Books](https://img.shields.io/badge/Apple_Books-000000?style=for-the-badge&logo=apple&logoColor=white)](https://books.apple.com/us/book/ai-agents-in-cybersecurity/id6751737181)
[![Amazon](https://img.shields.io/badge/Amazon-FF9900?style=for-the-badge&logo=amazon&logoColor=white)](https://a.co/d/07Fndacy)
[![GitHub](https://img.shields.io/badge/Companion_Code-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ai-agents-cybersecurity/complete)

<br clear="left" />

---

*Built by [Nic Cravino](https://github.com/ai-agents-cybersecurity) · AI/ML Engineering · Cybersecurity · Enterprise Automation*
