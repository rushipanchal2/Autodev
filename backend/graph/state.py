"""Shared state and structured schemas for the SDLC pipeline.

Phase 1 only uses `raw_input`, `user_stories`, `code_changes`. The remaining
fields are reserved for later phases and live here now so the graph can grow
without a breaking change to the state schema.
"""

from __future__ import annotations

from typing import TypedDict

from pydantic import BaseModel, Field


class UserStory(BaseModel):
    """A single, structured user story produced by the BA agent."""

    id: str = Field(description="Stable identifier, e.g. 'US-1'")
    title: str = Field(description="Short title for the story")
    story: str = Field(description="As a <role>, I want <goal>, so that <benefit>")
    acceptance_criteria: list[str] = Field(
        description="Testable acceptance criteria, each a single statement"
    )


class UserStories(BaseModel):
    """Wrapper so the LLM returns a list under a named field (structured output)."""

    stories: list[UserStory]


class CodeFile(BaseModel):
    """One generated source file."""

    path: str = Field(description="Relative file path, e.g. 'app/main.py'")
    content: str = Field(description="Full file contents")


class CodeChanges(BaseModel):
    """Wrapper for the Dev agent's structured output."""

    files: list[CodeFile]


class SDLCState(TypedDict, total=False):
    """State passed between nodes in the LangGraph pipeline."""

    raw_input: str               # from frontend / CLI (SASVA-style input)
    user_stories: list[dict]     # generated stories + acceptance criteria
    repo_path: str | None        # set for brownfield (Phase 3), None for greenfield
    code_changes: dict           # {path: content}
    test_cases: list[dict]       # Phase 2
    review_feedback: str | None  # Phase 4 loop
    iteration: int               # Phase 4 loop
