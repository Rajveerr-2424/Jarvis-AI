# 🤖 Jarvis AI

> A production-grade AI assistant inspired by Tony Stark's JARVIS, built with Python, Gemini, local LLMs, voice, memory, vision, and desktop automation.

> 🚧 Currently under active development.

---

## ✨ Features

### ✅ Current

- Gemini-powered conversational AI
- Modular architecture
- Configuration using `.env`
- Production-ready project structure
- Git versioning

### 🚧 Coming Soon

- Persistent memory (SQLite)
- Voice interaction
- Wake word detection
- Desktop automation
- Browser automation
- Vision (screen understanding)
- Local LLM support (Ollama)
- Multi-provider AI
- MCP tool integration
- Multi-agent architecture

---

# 🏗️ Project Structure

```text
Jarvis-AI/
│
├── assets/
├── automation/
├── brain/
├── config/
├── core/
├── logs/
├── mcp/
├── memory/
├── skills/
├── tests/
├── tools/
├── vision/
├── voice/
├── wakeword/
│
├── .env
├── .gitignore
├── main.py
├── pyproject.toml
└── README.md
```

---

# 🧠 Architecture

```
                 User
                  │
                  ▼
            Assistant Engine
                  │
                  ▼
            Brain Manager
        ┌─────────┴─────────┐
        │                   │
     Gemini             Ollama
                            │
                        Future Models
```

---

# 🚀 Installation

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

---

# 🔑 Environment Variables

Create a `.env`

```env
GEMINI_API_KEY=YOUR_API_KEY

MODEL=gemini-2.5-flash

USER_NAME=Rajveerr

ASSISTANT_NAME=Jarvis

TEMPERATURE=0.7

MAX_OUTPUT_TOKENS=2048
```

---

# ▶️ Run

```bash
python main.py
```

---

# 🛣️ Roadmap

## v0.1
- [x] Project architecture
- [x] Gemini integration
- [x] Interactive chat

## v0.2
- [ ] SQLite memory
- [ ] Conversation history
- [ ] Memory retrieval

## v0.3
- [ ] Voice input
- [ ] Text-to-Speech

## v0.4
- [ ] Wake word
- [ ] Always-on assistant

## v0.5
- [ ] Desktop automation
- [ ] File search
- [ ] Clipboard
- [ ] System controls

## v0.6
- [ ] Vision
- [ ] Screenshot analysis
- [ ] OCR

## v0.7
- [ ] Browser automation
- [ ] MCP tools

## v1.0
- [ ] Fully functional AI operating assistant

---

# 🛠️ Tech Stack

- Python
- Gemini API
- uv
- FastMCP
- Faster Whisper
- OpenWakeWord
- Playwright
- SQLite
- FAISS
- OpenCV

---

# 📌 Philosophy

Jarvis AI is designed with a modular architecture so components such as AI providers, memory, voice, automation, and vision can evolve independently.

The long-term goal is to create a production-grade AI operating assistant rather than a simple chatbot.

---

# 📜 License

This project is currently under development.

A license will be added before the first public release.

---

# 👨‍💻 Author

**Rajveerr Awachat**

Building the closest thing to a real-life JARVIS using free and open-source technologies.
