> 🚧 Currently under active development.
# 🤖 JARVIS AI

> A modular, extensible AI assistant inspired by Tony Stark's J.A.R.V.I.S.

JARVIS AI is a Python-based personal AI assistant built with a production-oriented architecture. It is designed to support multiple AI providers, persistent memory, voice interaction, desktop automation, and computer vision.

This project is focused on building a real AI operating assistant rather than a simple chatbot.

---

## ✨ Features

### ✅ Core Features

- 🧠 Modular AI Architecture
- 🔄 Multiple AI Provider Support
- ☁️ Google Gemini Integration
- 💻 Local Ollama Integration
- 📜 Rich Terminal Interface
- 📝 Structured Logging
- 💬 Conversation Management
- ⚙️ Environment-based Configuration
- 📦 Clean Project Architecture

---

## 🏗 Architecture

```
                    User
                      │
                      ▼
              Core Assistant
                      │
        ┌─────────────┴─────────────┐
        │                           │
 Conversation Manager        Memory Manager (WIP)
        │
        ▼
             Brain Manager
        │
  ┌─────┴──────────────┐
  │                    │
Gemini Provider   Ollama Provider
```

The assistant never communicates directly with a model.

Instead, every provider implements the same interface, allowing seamless switching between local and cloud models.

---

## 📂 Project Structure

```
Jarvis-AI/
│
├── brain/
│   ├── manager.py
│   ├── prompts.py
│   └── providers/
│       ├── base.py
│       ├── gemini.py
│       └── ollama.py
│
├── conversation/
│
├── core/
│
├── config/
│
├── ui/
│
├── memory/
│
├── vision/
│
├── voice/
│
├── automation/
│
├── wakeword/
│
├── tools/
│
├── logs/
│
├── database/
│
└── main.py
```

---

# 🚀 Tech Stack

### Language

- Python 3.13

### AI

- Google Gemini API
- Ollama

### Libraries

- google-genai
- ollama
- rich
- loguru
- prompt_toolkit
- pydantic-settings

### Configuration

- dotenv
- pydantic-settings

### Logging

- Loguru

### Terminal UI

- Rich
- Prompt Toolkit

---

# ⚡ Supported Providers

| Provider | Status |
|----------|--------|
| Gemini | ✅ |
| Ollama | ✅ |
| Groq | 🚧 Planned |
| OpenRouter | 🚧 Planned |

Switch providers using:

```env
AI_PROVIDER=gemini
```

or

```env
AI_PROVIDER=ollama
```

No code changes required.

---

# 📜 Logging

JARVIS uses structured logging powered by Loguru.

Example:

```
[19:43:11] INFO     assistant:start:42      Jarvis initialized
[19:43:15] INFO     assistant:start:58      User: Hello
[19:43:17] INFO     ollama:ask:39           Response generated
```

Logs are automatically stored in:

```
logs/jarvis.log
```

---

# 🎨 Terminal Interface

Built with Rich.

Features include:

- Colored prompts
- AI status dashboard
- Provider display
- Clean assistant responses
- Structured developer logs

---

# 🧠 Current Capabilities

- Chat with Gemini
- Chat with Ollama
- Multi-provider architecture
- Short-term conversation context
- Structured logging
- Interactive CLI

---

# 🚧 Roadmap

## Phase 1 ✅

- Project Setup
- Gemini Integration
- Rich UI
- Logging
- Conversation Manager

---

## Phase 2 ✅

- Brain Manager
- Provider Architecture
- Ollama Support
- Environment-based Provider Switching

---

## Phase 3 🚧

- SQLite Memory
- Remember / Recall
- User Preferences
- Conversation Persistence

---

## Phase 4 🚧

- Voice Input (STT)
- Voice Output (TTS)
- Wake Word Detection

---

## Phase 5 🚧

- Desktop Automation
- Browser Automation
- File Operations

---

## Phase 6 🚧

- Vision
- Screenshot Analysis
- OCR
- Image Understanding

---

## Phase 7 🚧

- MCP Integration
- Tool Calling
- Plugin System

---

# 🎯 Design Principles

- Modular Architecture
- Separation of Concerns
- Strategy Pattern
- Extensible Provider Layer
- Configuration-driven Design
- Clean Code
- Production-ready Structure

---

# 📈 Future Goals

- Long-term Memory
- Local Knowledge Base
- Hybrid Cloud + Local AI
- Smart Automation
- Personal Assistant Capabilities
- Multi-modal Understanding
- Real-time Voice Conversation

---

# 🛠 Installation

Clone the repository

```bash
git clone https://github.com/Rajveerr-2424/Jarvis-AI.git
cd Jarvis-AI
```

Create virtual environment

```bash
uv venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
uv sync
```

Create a `.env`

```env
AI_PROVIDER=ollama

OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=qwen2.5:3b

GEMINI_API_KEY=

USER_NAME=Rajveerr
ASSISTANT_NAME=Jarvis
```

Run

```bash
python main.py
```

---

# 🤝 Contributing

Contributions, ideas, and feature suggestions are welcome.

---

# 📄 License

MIT License

---

# 👨‍💻 Author

**Rajveerr Awachat**

Computer Science Engineer • AI Developer • Robotics Enthusiast

Building a real-world JARVIS from scratch.
