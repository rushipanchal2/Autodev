"""BA / Requirements agent (LLM #1).

Reads `raw_input` and produces structured `user_stories`.
"""

from __future__ import annotations

from ..llm import get_model
from ..state import SDLCState, UserStories

_SYSTEM_PROMPT = """You are a senior business analyst.
Turn the raw requirements into clear, atomic user stories.

Rules:
- Each story uses the form: "As a <role>, I want <goal>, so that <benefit>".
- Give each story a stable id (US-1, US-2, ...).
- Provide concrete, testable acceptance criteria for every story.
- Keep stories independently implementable; split anything compound.
"""


def ba_agent(state: SDLCState) -> dict:
    """LangGraph node: raw_input -> user_stories."""
    llm = get_model().with_structured_output(UserStories)
    result: UserStories = llm.invoke(
        [
            ("system", _SYSTEM_PROMPT),
            ("human", state["raw_input"]),
        ]
    )
    return {"user_stories": [s.model_dump() for s in result.stories]}
