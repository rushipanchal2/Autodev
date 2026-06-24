"""Unit tests for the BA agent."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from graph.agents.ba_agent import ba_agent
from graph.state import UserStories, UserStory


@pytest.fixture()
def mock_user_stories():
    return UserStories(
        stories=[
            UserStory(
                id="US-1",
                title="Add a task",
                story="As a user, I want to add a task, so that I can track it.",
                acceptance_criteria=["Task is saved", "Task has unique id"],
            )
        ]
    )


@patch("graph.agents.ba_agent.get_model")
def test_ba_agent_returns_user_stories(mock_get_model, mock_user_stories, sample_raw_input):
    mock_llm = MagicMock()
    mock_llm.with_structured_output.return_value.invoke.return_value = mock_user_stories
    mock_get_model.return_value = mock_llm

    result = ba_agent({"raw_input": sample_raw_input})

    assert "user_stories" in result
    assert len(result["user_stories"]) == 1
    assert result["user_stories"][0]["id"] == "US-1"


@patch("graph.agents.ba_agent.get_model")
def test_ba_agent_empty_stories(mock_get_model, sample_raw_input):
    mock_llm = MagicMock()
    mock_llm.with_structured_output.return_value.invoke.return_value = UserStories(stories=[])
    mock_get_model.return_value = mock_llm

    result = ba_agent({"raw_input": sample_raw_input})

    assert result["user_stories"] == []
