# SDLC Agent

A multi-agent system that turns plain-English requirements into working code using LangGraph and Azure OpenAI.

## Architecture

```
raw_input
   │
   ▼
BA Agent  →  user_stories
   │
   ▼
Dev Agent →  code_changes
   │
   ▼
QE Agent  →  test_cases        (Phase 2)
   │
   ▼
Router    →  review_feedback   (Phase 4)
```

## Project Structure

```
sdlc-agent/
├── backend/
│   ├── config/          # Centralised settings (loaded from .env)
│   ├── api/             # FastAPI routes (Phase 4)
│   │   └── routes/
│   ├── graph/           # LangGraph pipeline
│   │   ├── agents/      # BA, Dev, QE, Router nodes
│   │   ├── tools/       # File and repo tools (Phase 3)
│   │   ├── orchestration.py  # Graph wiring
│   │   ├── state.py     # Shared SDLCState schema
│   │   └── llm.py       # Shared model factory
│   ├── tests/           # Pytest test suite
│   │   ├── test_agents/
│   │   ├── test_api/
│   │   └── conftest.py
│   ├── output/          # Generated code written here (gitignored)
│   ├── main.py          # CLI entrypoint
│   ├── app.py           # FastAPI entrypoint (Phase 4)
│   ├── requirements.txt
│   ├── .env.example     # Copy to .env and fill in credentials
│   └── .gitignore
└── docs/                # Architecture docs
```

## Quick Start

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
cp .env.example .env            # fill in your Azure OpenAI credentials
python main.py
```

## Running Tests

```bash
cd backend
pytest tests/ -v
```

## Environment Variables

| Variable | Description |
|---|---|
| `AZURE_OPENAI_API_KEY` | Azure OpenAI API key |
| `AZURE_OPENAI_BASE_URL` | Endpoint, e.g. `https://<resource>.openai.azure.com/openai/v1` |
| `AZURE_OPENAI_MODEL` | Model deployment name, e.g. `gpt-4.1` |
| `LLM_TEMPERATURE` | Sampling temperature (default `0.2`) |

## Phases

| Phase | Status | Description |
|---|---|---|
| 1 | Done | BA + Dev agents, CLI runner |
| 2 | Planned | QE agent, pytest generation |
| 3 | Planned | Brownfield repo tools |
| 4 | Planned | FastAPI + SSE streaming |

## License

MIT — see [LICENSE](LICENSE)
