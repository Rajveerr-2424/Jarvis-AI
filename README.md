> 🚧 Currently under active development.

# JARVIS AI

> An intelligent AI assistant inspired by Tony Stark's JARVIS, designed to be modular, extensible, and capable of evolving into a fully autonomous desktop assistant.

> **Current Version:** v0.3.0 *(Pre-release)*

---

## Overview

JARVIS AI is a local-first AI assistant focused on:

- Artificial Intelligence
- Automation
- Programming Assistance
- Productivity
- Tool Execution
- Long-term Memory
- Extensible Architecture

Unlike a simple chatbot, JARVIS is designed as an AI operating framework where different subsystems (Memory, Tools, Providers, Commands, Conversation) work together to solve problems.

---

# Features

## AI Providers

- Ollama (Local LLM)
- Google Gemini
- Automatic Provider Fallback (Ollama → Gemini)

---

## Memory System

- Persistent SQLite Memory
- Memory Storage
- Memory Recall
- Memory Management
- Conversation Context

---

## Tool Framework

Current Built-in Tools

- Calculator

Architecture

- Tool Manager
- Tool Catalog
- Base Tool Abstraction

---

## Developer Commands

| Command | Description |
|----------|-------------|
| `/help` | Show available commands |
| `/status` | Display system status |
| `/provider` | Show active provider |
| `/model` | Show current model |
| `/memory` | List stored memories |
| `/forget` | Delete memory |
| `/history` | Show conversation history |
| `/tools` | Show registered tools |
| `/version` | Show version information |
| `/clear` | Clear conversation |
| `/cls` | Clear terminal |
| `/exit` | Exit JARVIS |

---

## User Interface

- Rich Terminal UI
- Colored Responses
- Colored Prompt
- Rich Tables
- Startup Dashboard
- Structured Logging

---

# Architecture

```
User
 │
 ▼
Assistant
 │
 ├── Commands
 ├── Tools
 ├── Memory
 ├── Conversation
 └── Brain
       │
       ├── Ollama
       └── Gemini
```

---

# Project Structure

```
Jarvis/
│
├── brain/
│   ├── manager.py
│   └── providers/
│
├── conversation/
│
├── config/
│
├── core/
│
├── memory/
│
├── tools/
│   ├── core/
│   └── calculator.py
│
├── ui/
│
├── logs/
│
├── main.py
├── README.md
└── CHANGELOG.md
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Jarvis-AI.git
```

Enter the project

```bash
cd Jarvis-AI
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

### Windows

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Configuration

Create a `.env`

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

- Multi-provider AI
- Persistent Memory
- Conversation Context
- Tool Framework
- Calculator Tool
- Rich Command Interface
- Automatic Provider Fallback

---

# Roadmap

## Phase 1 — Foundation ✅

- Project Structure
- Rich UI
- Logging
- Configuration

---

## Phase 2 — AI Core ✅

- Gemini Provider
- Ollama Provider
- Brain Manager
- Provider Abstraction

---

## Phase 3 — Memory ✅

- Persistent Memory
- SQLite Repository
- Conversation Manager

---

## Phase 4 — Tool Ecosystem *(In Progress)*

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

- Task Planner
- Streaming Responses
- Voice Assistant
- Vision Support
- Automation
- Multi-Agent System
- MCP Integration

---

# Version Status

| Version | Status |
|----------|--------|
| v0.1 | Foundation |
| v0.2 | AI Providers |
| v0.3 | Tool Framework |
| v0.4 | Tool Ecosystem *(Current Target)* |
| v1.0 | Stable Release |

---

# Contributing

Contributions, ideas, and discussions are welcome.

If you'd like to improve JARVIS, feel free to open an Issue or Pull Request.

---

# License

This project is licensed under the MIT License.

---

# Acknowledgements

Inspired by **J.A.R.V.I.S.** from the Marvel Cinematic Universe.

This project is built for learning, experimentation, and advancing practical AI engineering.
