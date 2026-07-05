> 🚧 **Currently under active development.**
>
> JARVIS AI is currently in its **pre-release stage**. The core architecture is actively evolving as new capabilities, tools, and intelligent systems are introduced.

# JARVIS AI

> An intelligent AI assistant inspired by **J.A.R.V.I.S.** from the Marvel Cinematic Universe, designed to be modular, extensible, and capable of evolving into a fully autonomous desktop assistant.

![Version](https://img.shields.io/badge/version-v0.3.2-AA0505?style=for-the-badge)
![Status](https://img.shields.io/badge/status-Pre--Release-orange?style=for-the-badge)
![Python](https://img.shields.io/badge/python-3.11+-blue?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

---

# Overview

Growing up, I was fascinated by **Tony Stark's J.A.R.V.I.S.**—not just because it could answer questions, but because it behaved like an intelligent system capable of reasoning, remembering, assisting, and interacting naturally.

Back in **2022**, I built my first "AI assistant" called **Health AI**, a simple Python project based entirely on hardcoded rules and conditional logic. It wasn't powered by large language models, but it sparked an interest in building something much more capable.

Today, with modern advances in AI, local language models, and intelligent software systems, that vision is finally achievable.

JARVIS AI is my attempt to build that vision from the ground up—not as another chatbot, but as a modular AI operating framework focused on learning modern AI engineering, software architecture, and intelligent automation.

Although many open-source AI assistants already exist, this project is intentionally built from scratch as a personal engineering journey. Every subsystem is designed, implemented, and understood piece by piece rather than simply integrating existing frameworks.

The goal isn't to build something revolutionary overnight.

The goal is to understand how intelligent assistants are engineered.

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

### Current Built-in Tools

- Calculator
- Time
- UUID Generator
- Password Generator
- Hash Generator
- Clipboard
- System Information
- File Tool

### Framework

- Base Tool Abstraction
- Tool Manager
- Tool Catalog
- Automatic Tool Dispatching
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
          ┌───────────┴───────────┐
          │                       │
     Slash Commands         Tool Requests
          │                       │
          ▼                       ▼
   Command Handler         Tool Manager
                                   │
                              Tool Catalog
                                   │
      ┌─────────────────────────────────────────────┐
      │ Calculator                                  │
      │ Time                                        │
      │ UUID                                        │
      │ Password                                    │
      │ Hash                                        │
      │ Clipboard                                   │
      │ System                                      │
      │ File                                        │
      └─────────────────────────────────────────────┘
                                   │
                              Brain Manager
                        ┌─────────────────────┐
                        │ Ollama              │
                        │ Gemini              │
                        └─────────────────────┘
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
│   ├── filesystem/
│   ├── calculator.py
│   ├── clipboard.py
│   ├── file.py
│   ├── hash.py
│   ├── password.py
│   ├── system.py
│   ├── time.py
│   └── uuid.py
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
git clone https://github.com/Rajveerr-2424/Jarvis-AI.git
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

Create a `.env` file in the project root.

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

## AI

- Multi-Provider AI
- Automatic Provider Fallback
- Local LLM Support (Ollama)
- Cloud LLM Support (Gemini)

---

## Memory

- Persistent SQLite Memory
- Conversation Context
- Memory Storage
- Memory Recall
- Memory Management

---

## Tool Framework

- Automatic Tool Dispatching
- Modular Tool Architecture
- Tool Manager
- Tool Catalog
- Base Tool Abstraction

---

## Built-in Tools

### Calculator

- Evaluate mathematical expressions

### Time

- Current Date
- Current Time
- Current Day

### UUID

- Generate UUIDs

### Password

- Generate secure passwords
- Configurable password length

### Hash

Supported algorithms:

- MD5
- SHA1
- SHA256
- SHA512

### Clipboard

- Read Clipboard
- Write Clipboard
- Clear Clipboard

### System

- Operating System
- Python Version
- Machine Information
- Processor Information

### File Tool

#### Directory Operations

- Show Current Directory
- List Files

#### File Operations

- Read Files
- Create Files
- Write Files
- Append Files
- Rename Files
- Copy Files
- Move Files
- Delete Files

#### Folder Operations

- Create Folders

---

# JARVIS Command Language (JCL)

JARVIS follows a structured command syntax for all tool interactions.

```text
<Action> <Resource> <Arguments>
```

Examples

```text
read file README.md

write file notes.txt Hello World

append file notes.txt Another line

create folder Projects

copy file report.pdf Backup/

move file report.pdf Archive/

delete file temp.txt
```

Frequently used commands also have short aliases.

| Command | Alias |
|----------|-------|
| read file | `rf` |
| create file | `cf` |
| write file | `wf` |
| append file | `af` |
| rename file | `ren` |
| copy file | `cp` |
| move file | `mv` |
| delete file | `df` |
| create folder | `md` |
| current directory | `pwd` |
| list files | `ls` |

> **Note**
>
> Generic verbs such as `write`, `delete`, and `open` are intentionally reserved for future system-wide capabilities. Tool commands always specify the target resource, such as `write file` or `delete file`, making the command language consistent and scalable.

---

# Current Status

**Current Version:** **v0.3.2 (Pre-release)**

Current implementation includes:

- Modular AI Architecture
- Multi-Provider Support
- Persistent Memory
- Conversation Manager
- Rich Terminal Interface
- Developer Command System
- Modular Tool Framework
- Eight Built-in Tools
- Secure Local Filesystem Operations

The next milestone is **v0.4.0 – Tool Ecosystem**, focused on polishing the existing tools, improving stability, expanding documentation, and preparing the architecture for the Planner Engine introduced in **v0.5**.

---

# Roadmap

## ✅ Phase 1 — Foundation

Completed

- Project Structure
- Configuration System
- Rich Terminal UI
- Logging
- Environment Management

---

## ✅ Phase 2 — AI Core

Completed

- Gemini Provider
- Ollama Provider
- Provider Manager
- Automatic Provider Fallback

---

## ✅ Phase 3 — Memory

Completed

- SQLite Memory
- Memory Repository
- Memory Service
- Conversation Manager

---

## 🚧 Phase 4 — Tool Ecosystem

Completed

- Tool Framework
- Tool Manager
- Tool Catalog
- Calculator Tool
- Time Tool
- UUID Tool
- Password Generator
- Hash Tool
- Clipboard Tool
- System Information Tool
- File Tool

Current Focus

- Tool Documentation
- Stability Improvements
- Comprehensive Testing
- Browser Tool

---

## 🔜 Phase 5 — Planning Engine

Planned

- Command Parser
- Tool Registry
- JARVIS Command Language Routing
- Planner Engine
- Multi-Step Task Execution
- Tool Chaining

---

## 🔜 Phase 6 — Streaming

Planned

- Token Streaming
- Live Response Rendering
- Streaming Providers
- Improved Terminal Experience

---

## 🔜 Phase 7 — Voice

Planned

- Speech-to-Text
- Text-to-Speech
- Wake Word Detection
- Natural Voice Conversations

---

## 🔜 Phase 8 — Vision

Planned

- OCR
- Image Understanding
- Screenshot Analysis
- Camera Support

---

## 🔜 Phase 9 — Automation

Planned

- Task Scheduler
- Background Jobs
- Reminder System
- Workflow Automation

---

## 🔜 Phase 10 — Multi-Agent System

Planned

- Planner Agent
- Coding Agent
- Research Agent
- Browser Agent
- Task Delegation

---

## 🔜 Phase 11 — MCP Integration

Planned

- GitHub
- Gmail
- Google Calendar
- Browser
- Databases
- External Services

---

# Version Roadmap

| Version | Milestone |
|----------|-----------|
| **v0.1** | Foundation |
| **v0.2** | AI Providers |
| **v0.3** | Tool Framework |
| **v0.4** | Tool Ecosystem |
| **v0.5** | Planning Engine |
| **v0.6** | Streaming |
| **v0.7** | Voice |
| **v0.8** | Vision |
| **v0.9** | Automation |
| **v1.0** | Stable Release |

---

# Contributing

JARVIS AI is currently a **personal research and learning project**.

While the repository is public, active development is currently maintained by the author during the pre-release phase.

Suggestions, discussions, feature ideas, and bug reports are always welcome through **GitHub Issues**.

If you'd like to contribute:

- Fork the repository
- Create a feature branch
- Make your changes
- Submit a Pull Request

Please ensure new code follows the existing project structure and coding style.

---

# License

This project is licensed under the **MIT License**.

See the **LICENSE** file for more information.

---

# Acknowledgements

Inspired by **J.A.R.V.I.S.** from the Marvel Cinematic Universe.

This project began in **2022** with a simple Python experiment called **Health AI**—a rule-based assistant built entirely with conditional logic. Although it wasn't powered by modern language models, it sparked a lasting interest in building intelligent assistants.

Today, JARVIS AI represents the next stage of that journey.

Rather than relying heavily on existing assistant frameworks, this project focuses on understanding and implementing each subsystem from first principles. Every provider, memory system, tool, command, and architectural decision is an opportunity to learn more about modern AI engineering.

The long-term vision is to build a capable desktop AI assistant that can reason, remember, use tools, automate workflows, and assist with everyday computing tasks through a modular and extensible architecture.

---

# Tech Stack

### Language

- Python 3.11+

### AI Providers

- Ollama
- Google Gemini

### Database

- SQLite

### Terminal UI

- Rich
- Prompt Toolkit

### Configuration

- python-dotenv

### Logging

- Loguru

---

# Why JARVIS AI?

This project is being built to explore and understand:

- AI System Architecture
- LLM Integration
- Tool Calling
- Long-Term Memory
- Agent Design
- Local AI
- Software Engineering
- Intelligent Automation

The emphasis is not only on creating an AI assistant, but on learning how such systems are designed, built, and evolve over time.

---


## Star the Repository

If you find this project interesting or would like to follow its progress, consider giving it a ⭐ on GitHub.

Your support helps motivate continued development and makes it easier for others to discover the project.

---

> **"Inspired by J.A.R.V.I.S. Built to Learn. Engineered to Evolve."**