"""Dev agent (LLM #2).

Phase 1 (greenfield only): reads `user_stories` and produces full source files
as structured `code_changes` ({path: content}). Brownfield/tools come in Phase 3.
"""

from __future__ import annotations

import json

from ..llm import get_model
from ..state import CodeChanges, SDLCState

_SYSTEM_PROMPT = """You are a senior software engineer building a new (greenfield) project.
Implement the given user stories as a small, runnable codebase.

Rules:
- Output complete files with relative paths (e.g. 'app/main.py', 'README.md').
- Satisfy every acceptance criterion across the stories.
- Prefer a single coherent language/stack; keep it minimal but runnable.
- Include a short README and any needed config/dependency file.
- Do not include explanations outside the files themselves.
"""


def dev_agent(state: SDLCState) -> dict:
    """LangGraph node: user_stories -> code_changes ({path: content})."""
    llm = get_model().with_structured_output(CodeChanges)
    stories = json.dumps(state["user_stories"], indent=2)
    result: CodeChanges = llm.invoke(
        [
            ("system", _SYSTEM_PROMPT),
            ("human", f"Implement these user stories:\n\n{stories}"),
        ]
    )
    return {"code_changes": {f.path: f.content for f in result.files}}
