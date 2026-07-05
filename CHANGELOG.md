# Changelog

All notable changes to JARVIS AI will be documented in this file.

The format is inspired by Keep a Changelog and follows Semantic Versioning.

---

## [Unreleased]

### Planned

#### Architecture
- Command Parser.
- Tool Registry.
- JARVIS Command Language (JCL) routing.
- Planner Engine.
- Multi-step task execution.
- Tool chaining.

#### Future
- Voice support.
- Vision support.
- Streaming responses.
- Automation framework.

---

## [0.3.2] - 2026-07-05

### Added

#### File Tool
- Added modular File Tool architecture.
- Added current working directory command.
- Added directory listing command.
- Added secure file reading.
- Added file creation.
- Added file writing.
- Added file append operation.
- Added folder creation.
- Added file renaming.
- Added file copying.
- Added file moving.
- Added file deletion.
- Added workspace path validation.

#### Command Aliases
- `rf`
- `cf`
- `wf`
- `af`
- `ren`
- `cp`
- `mv`
- `df`
- `md`
- `pwd`
- `ls`

### Improved

#### File Tool
- Refactored File Tool to use a command dispatcher.
- Split filesystem operations into dedicated modules.
- Improved help documentation.
- Improved command routing.
- Standardized filesystem commands.
- Standardized explicit resource-based commands:
  - `read file`
  - `create file`
  - `write file`
  - `append file`
  - `rename file`
  - `copy file`
  - `move file`
  - `delete file`
  - `create folder`

### Security

- Restricted filesystem operations to the current workspace.
- Prevented directory traversal (`..`).
- Added safe path resolution using `pathlib`.
- Prevented overwriting existing files during copy and move operations.
- Added validation for filesystem operations.

### Architecture

- Adopted the **JARVIS Command Language (JCL)**.

```
<Action> <Resource> <Arguments>
```

Examples:

```
read file notes.txt
write file notes.txt Hello
append file notes.txt World
create folder Projects
delete file notes.txt
```

- Reserved generic verbs (`write`, `delete`, `open`, etc.) for future system-wide resources.
- Standardized explicit resource-based commands.
- Deferred the centralized `CommandParser` architecture to **v0.5**.

---

## [0.3.0] - 2026-07-05

### Added

#### AI Core
- Multi-provider AI architecture.
- Gemini provider integration.
- Ollama provider integration.
- Automatic provider fallback (Ollama → Gemini).
- Runtime provider and model tracking.

#### Memory
- Persistent SQLite-based memory.
- Memory repository layer.
- Memory service abstraction.
- Automatic memory storage.
- Memory retrieval system.
- Memory management commands.

#### Conversation
- Conversation manager.
- Short-term conversation history.
- Context-aware AI responses.

#### Tool Framework
- BaseTool abstraction.
- ToolManager.
- Tool Catalog.
- CalculatorTool.
- Tool metadata support.
- Tool enable/disable architecture.

#### Commands
- `/help`
- `/status`
- `/provider`
- `/model`
- `/memory`
- `/forget`
- `/history`
- `/version`
- `/clear`
- `/cls`
- `/tools`
- `/exit`

#### Terminal UI
- Rich-powered terminal interface.
- Colored user prompt.
- Colored JARVIS responses.
- Status dashboard.
- Rich tables.
- Startup banner.

#### Logging
- Structured logging using Loguru.
- File logging.
- Console logging.
- Improved log formatting.

### Improved

- Refactored project into a modular architecture.
- Introduced provider abstraction layer.
- Introduced memory abstraction.
- Introduced tool abstraction.
- Improved command handling.
- Improved terminal experience.
- Cleaner project structure.
- Better separation of responsibilities.
- Improved code readability and maintainability.

### Fixed

- Provider switching issues.
- Conversation context handling.
- Ollama integration issues.
- Tool execution flow.
- Command handling edge cases.
- Multiple UI improvements.

---

## [0.2.0]

### Added

#### AI
- Gemini API integration.
- Ollama integration.
- BrainManager.
- BaseProvider abstraction.

#### Conversation
- Session conversation history.
- Context window support.

#### UI
- Interactive CLI.
- Rich console output.

### Improved

- Better prompt engineering.
- Improved response formatting.

---

## [0.1.0]

### Initial Release

#### Core
- Initial JARVIS project structure.
- Configuration system.
- Main application loop.
- Basic AI interaction.
- Environment variable support.

#### Developer Experience
- Logging system.
- Project modularization.
- Initial documentation.