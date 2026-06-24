# Autodev

**Autodev** automates the entire software development lifecycle (SDLC) — from requirement gathering all the way to deployment — using the **BMAD method** (Breakthrough Method of Agile AI-Driven Development).

Instead of a single monolithic prompt, Autodev orchestrates a team of specialized AI agents that hand work off to each other the way a real agile team does: an analyst gathers requirements, a PM writes the PRD, an architect designs the system, a scrum master slices work into stories, developers implement them, and a QA agent tests the result before deployment.

---

## What it does

Autodev takes a high-level product idea and drives it through the full lifecycle:

```
Idea ──▶ Requirements ──▶ PRD ──▶ Architecture ──▶ Stories ──▶ Implementation ──▶ QA ──▶ Deployment
```

| Stage | BMAD Agent | Output |
|-------|-----------|--------|
| Requirement gathering | Analyst | Brief / requirements doc |
| Product definition | Product Manager | `docs/prd/` PRD |
| System design | Architect | `docs/architecture/` design docs |
| Task breakdown | Scrum Master | `docs/stories/` user stories |
| Implementation | Developer | Source code + commits |
| Testing | QA | Test suite + QA report |
| Release | DevOps | Deployment artifacts |

## The BMAD method

[BMAD](https://github.com/bmad-code-org/BMAD-METHOD) structures AI-driven development around two ideas:

1. **Agentic planning** — dedicated Analyst, PM, and Architect agents produce detailed, consistent planning artifacts (PRD, architecture) instead of generic prompts.
2. **Context-engineered development** — the Scrum Master turns those plans into hyper-detailed story files that carry full context into implementation, so the Dev and QA agents never lose the thread.

Autodev wires these agents into an automated pipeline so the handoffs happen without manual copy-paste.

## Project structure

```
autodev/
├── src/autodev/
│   ├── agents/        # One module per BMAD agent (analyst, pm, architect, sm, dev, qa)
│   ├── pipeline/      # Orchestration: sequences agents and passes context between stages
│   └── core/          # Shared: LLM client, config loader, artifact store
├── docs/
│   ├── prd/           # Generated PRDs
│   ├── stories/       # Generated user stories
│   └── architecture/  # Generated architecture docs
├── config/            # Pipeline + agent configuration
├── tests/
└── .github/workflows/ # CI
```

## Quick start

> ⚠️ This is an early scaffold — most modules are stubs. See [Roadmap](#roadmap).

```bash
# 1. Clone
git clone https://github.com/<your-username>/autodev.git
cd autodev

# 2. Set up environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 3. Configure secrets (never commit these)
cp .env.example .env             # then fill in your API key(s)

# 4. Run the pipeline on an idea
python -m autodev "Build a URL shortener with analytics"
```

## Configuration

Secrets are read from environment variables only (see `.env.example`):

| Variable | Purpose |
|----------|---------|
| `ANTHROPIC_API_KEY` | LLM backing the BMAD agents |

Pipeline behavior (which agents run, model, temperature) is configured in `config/pipeline.yaml`.

## Roadmap

- [ ] Define `ProjectState` shared context object
- [ ] Implement each BMAD agent (analyst → qa)
- [ ] Wire the orchestration pipeline with handoffs
- [ ] Artifact persistence to `docs/`
- [ ] QA gate before deployment stage
- [ ] CI workflow

## Contributing

This is a solo/early-stage project. Issues and PRs welcome once the core pipeline lands.

## License

MIT — see [LICENSE](LICENSE).
