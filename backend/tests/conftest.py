"""Shared pytest fixtures for the SDLC agent test suite."""

from __future__ import annotations

import pytest


@pytest.fixture()
def sample_raw_input() -> str:
    return (
        "Scope: A command-line TODO app for a single user.\n"
        "Actors: A user who manages personal tasks.\n"
        "Steps: Add a task, list all tasks, mark done, delete a task.\n"
        "Value: Helps the user keep track of what needs to be done.\n"
        "Assumptions: Tasks stored in a local JSON file. No auth needed."
    )


@pytest.fixture()
def sample_user_stories() -> list[dict]:
    return [
        {
            "id": "US-1",
            "title": "Add a task",
            "story": "As a user, I want to add a task, so that I can track it.",
            "acceptance_criteria": ["Task is saved to JSON", "Task has a unique id"],
        }
    ]
