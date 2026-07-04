> 🚧 **Currently under active development.**
>
> JARVIS AI is in its pre-release stage. The architecture is evolving rapidly as new capabilities are added.

# JARVIS AI

> An intelligent AI assistant inspired by **J.A.R.V.I.S.** from the Marvel Cinematic Universe, designed to be modular, extensible, and capable of evolving into a fully autonomous desktop assistant.

![Version](https://img.shields.io/badge/version-v0.3.0-AA0505?style=for-the-badge)
![Status](https://img.shields.io/badge/status-Pre--Release-orange?style=for-the-badge)
![Python](https://img.shields.io/badge/python-3.11+-blue?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

---

# Overview

JARVIS AI is a **local-first AI assistant** focused on building a robust software architecture rather than simply wrapping an LLM.

The long-term vision is to create a modular assistant capable of reasoning, remembering, using tools, planning tasks, and interacting naturally with users.

Current focus areas include:

- Artificial Intelligence
- Local LLMs
- Automation
- Programming Assistance
- Long-Term Memory
- Modular Architecture
- Extensible Tool Ecosystem

Unlike a traditional chatbot, JARVIS is built as an **AI Operating Framework**, where independent subsystems collaborate to solve user requests.

---

# Features

## AI Providers

- Ollama (Local LLM)
- Google Gemini
- Automatic Provider Fallback (Ollama → Gemini)

---

## Memory

- Persistent SQLite Memory
- Memory Storage
- Memory Recall
- Memory Management
- Conversation Context

---

## Tool Framework

Current Tool

- Calculator

Framework

- Base Tool Abstraction
- Tool Manager
- Tool Catalog
- Modular Tool Architecture

---

## Developer Commands

| Command | Description |
|----------|-------------|
| `/help` | Show all available commands |
| `/status` | Display current system status |
| `/provider` | Show active AI provider |
| `/model` | Show current AI model |
| `/memory` | Show stored memories |
| `/forget` | Delete memories |
| `/history` | Show conversation history |
| `/tools` | Show registered tools |
| `/version` | Show version information |
| `/clear` | Clear conversation |
| `/cls` | Clear terminal |
| `/exit` | Exit JARVIS |

---

## User Interface

- Rich Terminal UI
- Colored User Prompt
- Colored AI Responses
- Rich Tables
- Startup Dashboard
- Structured Logging

---

# Architecture

```text
                User
                  │
                  ▼
             JARVIS Core
                  │
 ┌──────────┬──────────┬──────────┬──────────┐
 ▼          ▼          ▼          ▼
Commands   Memory   Conversation  Tools
                                │
                                ▼
                          Tool Manager
                                │
                                ▼
                          Tool Catalog
                                │
                                ▼
                        Calculator Tool
                  │
                  ▼
             Brain Manager
                  │
        ┌─────────┴─────────┐
        ▼                   ▼
    Ollama             Gemini
```

---

# Project Structure

```text
Jarvis/
│
├── brain/
│   ├── manager.py
│   └── providers/
│
├── config/
│
├── conversation/
│
├── core/
│
├── logs/
│
├── memory/
│
├── tools/
│   ├── core/
│   └── calculator.py
│
├── ui/
│
├── main.py
├── README.md
├── CHANGELOG.md
└── LICENSE
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/<YOUR_USERNAME>/Jarvis-AI.git
```

Move into the project

```bash
cd Jarvis-AI
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Configuration

Create a `.env` file

```env
AI_PROVIDER=auto

OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=qwen2.5:3b

GEMINI_API_KEY=YOUR_API_KEY
GEMINI_MODEL=gemini-2.5-flash

TEMPERATURE=0.7
MAX_OUTPUT_TOKENS=1024
```

---

# Running JARVIS

```bash
python main.py
```

---

# Current Capabilities

- Multi-Provider AI
- Automatic Provider Fallback
- Persistent Memory
- Conversation Management
- Modular Tool Framework
- Calculator Tool
- Rich CLI
- Structured Logging

---

# Roadmap

## ✅ Phase 1 — Foundation

- Project Structure
- Rich UI
- Configuration
- Logging

---

## ✅ Phase 2 — AI Core

- Gemini Provider
- Ollama Provider
- Brain Manager
- Provider Abstraction

---

## ✅ Phase 3 — Memory

- SQLite Memory
- Memory Repository
- Memory Service
- Conversation Manager

---

## 🚧 Phase 4 — Tool Ecosystem

Completed

- Tool Framework
- Tool Catalog
- Calculator Tool

Upcoming

- Time Tool
- UUID Tool
- Password Tool
- Hash Tool
- Clipboard Tool
- System Tool
- File Tool
- Browser Tool

---

## Future Milestones

- Intelligent Planner
- Streaming Responses
- Voice Assistant
- Vision Support
- Automation
- Multi-Agent System
- MCP Integration

---

# Version Roadmap

| Version | Milestone |
|----------|-----------|
| v0.1 | Foundation |
| v0.2 | AI Providers |
| v0.3 | Tool Framework |
| v0.4 | Tool Ecosystem |
| v0.5 | Planning Engine |
| v0.6 | Streaming |
| v0.7 | Voice |
| v0.8 | Vision |
| v0.9 | Automation |
| v1.0 | Stable Release |

---


# Contributing

JARVIS AI is currently a **personal research and learning project**.

While the repository is public, **active development is maintained solely by the author** during the pre-release phase.

Suggestions, discussions, feature ideas, and bug reports are always welcome through GitHub Issues.

---

# License

This project is licensed under the **MIT License**.

See the `LICENSE` file for details.

---

# Acknowledgements

Inspired by **J.A.R.V.I.S.** from the Marvel Cinematic Universe.

This journey began in **2022** with a simple **Health AI Python Bot** built using hardcoded Python logic. While it wasn't powered by modern AI, it sparked an interest in creating intelligent assistants.

Today, JARVIS AI represents the next step in that journey—building a modular AI assistant from the ground up to better understand modern AI engineering, system architecture, and intelligent automation.

---

> **"Inspired by J.A.R.V.I.S. Built to Learn."**
