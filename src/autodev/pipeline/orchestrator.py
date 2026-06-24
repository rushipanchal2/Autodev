"""Orchestrates the BMAD agent pipeline.

Sequences the SDLC stages and passes the shared project context from one
agent to the next. This is a skeleton — each stage currently just announces
itself. Fill in the agents under ``autodev.agents`` and replace the prints
with real calls.
"""

from dataclasses import dataclass, field

# Ordered BMAD stages: (stage name, BMAD agent role).
STAGES: list[tuple[str, str]] = [
    ("requirements", "analyst"),
    ("prd", "pm"),
    ("architecture", "architect"),
    ("stories", "sm"),
    ("implementation", "dev"),
    ("qa", "qa"),
    ("deployment", "devops"),
]


@dataclass
class ProjectState:
    """Shared context threaded through every stage."""

    idea: str
    artifacts: dict[str, str] = field(default_factory=dict)


def run_pipeline(idea: str) -> ProjectState:
    """Drive ``idea`` through every SDLC stage and return the final state."""
    state = ProjectState(idea=idea)
    print(f"Autodev: starting pipeline for: {idea!r}\n")
    for stage, agent in STAGES:
        print(f"  [{agent:<9}] {stage} … (not yet implemented)")
        # TODO: dispatch to autodev.agents.<agent> and store its output in
        # state.artifacts[stage].
    print("\nAutodev: pipeline complete (skeleton run).")
    return state
