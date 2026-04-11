## Hi there 👋

<!--

**Here are some ideas to get you started:**

🙋‍♀️ A short introduction - what is your organization all about?
🌈 Contribution guidelines - how can the commun# GitHub Reorganization — Execution Plan

**Personal account:** `ai-agents-cybersecurity`
**New public org:** `sw30labs`
**Private org (customer):** `the-ai-orchestrator` — untouched

---

## Phase 1: Archive Sweep

Run these from any terminal with `gh` CLI authenticated:

```bash
# Repos to archive (legacy Autogen, superseded versions, dead projects)
gh repo archive ai-agents-cybersecurity/AutogenSecurityScanner --yes
gh repo archive ai-agents-cybersecurity/AutoGen-Proteus-Core --yes
gh repo archive ai-agents-cybersecurity/AutogenGeminiChatCompletionClient --yes
gh repo archive ai-agents-cybersecurity/LangGraph-WebPilot --yes
gh repo archive ai-agents-cybersecurity/EFI-NEW-V2 --yes
gh repo archive ai-agents-cybersecurity/EfiNewsletter --yes
gh repo archive ai-agents-cybersecurity/PascalNewsletter --yes
gh repo archive ai-agents-cybersecurity/lg-ported-pascal-newsletter --yes
gh repo archive ai-agents-cybersecurity/pascalbornet-n8n --yes
gh repo archive ai-agents-cybersecurity/book-buddy --yes
gh repo archive ai-agents-cybersecurity/docx_ole_extract --yes
gh repo archive ai-agents-cybersecurity/Agentic-AI-Book-Editorial-Agency --yes
```

---

## Phase 2: Transfer Public Repos to sw30labs

> **Prerequisite:** Create the `sw30labs` org first, then run these.
> GitHub will auto-create redirects from old URLs.

```bash
# 🔒 Cybersecurity & Pentesting
gh repo transfer ai-agents-cybersecurity/TSLIT sw30labs --yes
gh repo transfer ai-agents-cybersecurity/strixresearch sw30labs --yes
gh repo transfer ai-agents-cybersecurity/pentest-regulatory-intel sw30labs --yes
gh repo transfer ai-agents-cybersecurity/agentic-ai-pentesting sw30labs --yes

# 🛡️ OSCAL & Compliance
gh repo transfer ai-agents-cybersecurity/oscal-digital-twin-playground sw30labs --yes
gh repo transfer ai-agents-cybersecurity/oscal-agent-guardrails sw30labs --yes
gh repo transfer ai-agents-cybersecurity/oscal-zero-trust-lens sw30labs --yes
gh repo transfer ai-agents-cybersecurity/oscal-agent-lab sw30labs --yes
gh repo transfer ai-agents-cybersecurity/oscal-cac-playgd sw30labs --yes

# 🤖 Agentic Frameworks
gh repo transfer ai-agents-cybersecurity/agent-stack sw30labs --yes
gh repo transfer ai-agents-cybersecurity/deepagent-azure-cli sw30labs --yes
gh repo transfer ai-agents-cybersecurity/N8n2langraph sw30labs --yes
gh repo transfer ai-agents-cybersecurity/sst-autoresearch sw30labs --yes
gh repo transfer ai-agents-cybersecurity/projectpulse sw30labs --yes

# ⚡ Local Inference & MLX
gh repo transfer ai-agents-cybersecurity/tars-ai sw30labs --yes
gh repo transfer ai-agents-cybersecurity/screenlens sw30labs --yes
gh repo transfer ai-agents-cybersecurity/qwenbench-mlx sw30labs --yes
gh repo transfer ai-agents-cybersecurity/mlx-distillation-explained sw30labs --yes
gh repo transfer ai-agents-cybersecurity/local-mlx-responsesAPI-server sw30labs --yes
gh repo transfer ai-agents-cybersecurity/audiobook_generator sw30labs --yes
gh repo transfer ai-agents-cybersecurity/QWEN3-VL-Python-OCR-Script-MLX sw30labs --yes
gh repo transfer ai-agents-cybersecurity/MLX-YouTubeScribe sw30labs --yes

# 🔧 Utilities
gh repo transfer ai-agents-cybersecurity/gitnexus_fleet sw30labs --yes
```

---

## Phase 3: Pin Repos on sw30labs

After transfers, pin these 4 on the org profile:

1. **TSLIT** — flagship security tool
2. **pentest-regulatory-intel** — highest stars (5)
3. **agent-stack** — architecture visualization
4. **tars-ai** — local voice agent demo

---

## Phase 4: Profile READMEs

### 4a. sw30labs Org Profile README

Create repo: `sw30labs/.github` → file: `profile/README.md`

```markdown
# SW3.0 Labs

**Building the inference layer as the primary enterprise operating layer.**

We build open-source tools at the intersection of AI agents, cybersecurity, and local inference — with a bias toward production-grade security, Apple Silicon optimization, and agentic automation.

---

### 🔒 AI Security & Pentesting

| Repo | What it does |
|------|-------------|
| [TSLIT](https://github.com/sw30labs/TSLIT) | Time-Shift LLM Integrity Tester — 3,840-prompt adversarial evaluation harness for local LLMs |
| [pentest-regulatory-intel](https://github.com/sw30labs/pentest-regulatory-intel) | AI pentesting regulatory intelligence across 20+ financial jurisdictions |
| [strixresearch](https://github.com/sw30labs/strixresearch) | Research docs for Strix autonomous pentesting platform |
| [agentic-ai-pentesting](https://github.com/sw30labs/agentic-ai-pentesting) | Agentic AI for Layer 7 penetration testing |

### 🛡️ OSCAL & Compliance-as-Code

| Repo | What it does |
|------|-------------|
| [oscal-agent-guardrails](https://github.com/sw30labs/oscal-agent-guardrails) | OSCAL controls as policy guardrails for LangGraph agents |
| [oscal-digital-twin-playground](https://github.com/sw30labs/oscal-digital-twin-playground) | OSCAL-backed digital twin with risk assessment agents |
| [oscal-zero-trust-lens](https://github.com/sw30labs/oscal-zero-trust-lens) | Zero Trust semantic overlay on OSCAL controls |
| [oscal-agent-lab](https://github.com/sw30labs/oscal-agent-lab) | Multi-agent copilot for OSCAL catalogs and SSPs |
| [oscal-cac-playgd](https://github.com/sw30labs/oscal-cac-playgd) | Compliance-as-code CLI using real NIST OSCAL JSON |

### 🤖 Agentic Frameworks & Tooling

| Repo | What it does |
|------|-------------|
| [agent-stack](https://github.com/sw30labs/agent-stack) | Interactive 10-layer Agent Stack architecture visualization |
| [deepagent-azure-cli](https://github.com/sw30labs/deepagent-azure-cli) | LangChain DeepAgents + Azure OpenAI coding assistant CLI |
| [N8n2langraph](https://github.com/sw30labs/N8n2langraph) | Convert n8n workflows to standalone LangGraph scripts |
| [sst-autoresearch](https://github.com/sw30labs/sst-autoresearch) | Autonomous research pipeline |
| [projectpulse](https://github.com/sw30labs/projectpulse) | SAP meetings → knowledge base + podcast via LangGraph |

### ⚡ Local Inference on Apple Silicon

| Repo | What it does |
|------|-------------|
| [tars-ai](https://github.com/sw30labs/tars-ai) | Talk to TARS — fully local voice agent on MLX, no API keys |
| [screenlens](https://github.com/sw30labs/screenlens) | Local video scene intelligence for Apple Silicon |
| [qwenbench-mlx](https://github.com/sw30labs/qwenbench-mlx) | Benchmark the full Qwen 3.5 family (0.8B–35B) on Apple Silicon |
| [mlx-distillation-explained](https://github.com/sw30labs/mlx-distillation-explained) | Educational: model distillation with Claude teacher + MLX student |
| [local-mlx-responsesAPI-server](https://github.com/sw30labs/local-mlx-responsesAPI-server) | OpenAI-compatible local inference server via MLX |
| [audiobook_generator](https://github.com/sw30labs/audiobook_generator) | Books → audiobooks with Qwen3-TTS + LangGraph |
| [QWEN3-VL-Python-OCR-Script-MLX](https://github.com/sw30labs/QWEN3-VL-Python-OCR-Script-MLX) | Image captioning with local MLX vision-language models |
| [MLX-YouTubeScribe](https://github.com/sw30labs/MLX-YouTubeScribe) | Audio/video transcription with WhisperX |

### 🔧 Developer Tools

| Repo | What it does |
|------|-------------|
| [gitnexus_fleet](https://github.com/sw30labs/gitnexus_fleet) | Clone, index, and query your entire GitHub fleet via MCP |

---

### 📖 Book

**[AI Agents in Cybersecurity](https://github.com/ai-agents-cybersecurity/complete)** — published book with companion code, available on the author's personal GitHub.

---

*Built by [Nic Cravino](https://github.com/ai-agents-cybersecurity) · AI/ML Engineering · Cybersecurity · Enterprise Automation*
```

---

### 4b. Personal Account Profile README

Create repo: `ai-agents-cybersecurity/ai-agents-cybersecurity` → file: `README.md`

```markdown
# Hey, I'm Nic 👋

AI/ML engineer and cybersecurity practitioner building at the intersection of agentic AI, LLM security, and local inference.

**📖 Author** of [AI Agents in Cybersecurity](https://github.com/ai-agents-cybersecurity/complete)

**🔬 Open-source work** lives at **[SW3.0 Labs](https://github.com/sw30labs)** — AI security tools, OSCAL compliance-as-code, agentic frameworks, and Apple Silicon inference.

**🔒 Current focus:** [TSLIT](https://github.com/sw30labs/TSLIT) — adversarial evaluation harness for local LLMs, detecting backdoors, affiliation bias, and temporal logic bombs.

---

### Elsewhere

- 🏢 Enterprise AI/ML consulting — Azure, LangChain, LangGraph
- ✍️ Writing on [LinkedIn](https://linkedin.com) about SW3.0 and the inference-first enterprise
- 🔧 Car stuff: Hummer H2 with long tubes, cat delete, CAI & HP Tuners
```ity get involved?
👩‍💻 Useful resources - where can the community find your docs? Is there anything else the community should know?
🍿 Fun facts - what does your team eat for breakfast?
🧙 Remember, you can do mighty things with the power of [Markdown](https://docs.github.com/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
-->
