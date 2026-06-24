"""Tests for the LangGraph orchestration pipeline."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from graph.orchestration import build_graph


@patch("graph.agents.dev_agent.get_model")
@patch("graph.agents.ba_agent.get_model")
def test_build_graph_returns_compiled_graph(mock_ba_model, mock_dev_model):
    graph = build_graph()
    assert graph is not None


@patch("graph.agents.dev_agent.get_model")
@patch("graph.agents.ba_agent.get_model")
def test_graph_invoke_produces_user_stories_and_code(
    mock_ba_model, mock_dev_model, sample_raw_input
):
    from graph.state import CodeChanges, CodeFile, UserStories, UserStory

    ba_result = UserStories(
        stories=[
            UserStory(
                id="US-1",
                title="Add task",
                story="As a user, I want to add a task.",
                acceptance_criteria=["Task saved"],
            )
        ]
    )
    dev_result = CodeChanges(files=[CodeFile(path="main.py", content="pass")])

    mock_ba_llm = MagicMock()
    mock_ba_llm.with_structured_output.return_value.invoke.return_value = ba_result
    mock_ba_model.return_value = mock_ba_llm

    mock_dev_llm = MagicMock()
    mock_dev_llm.with_structured_output.return_value.invoke.return_value = dev_result
    mock_dev_model.return_value = mock_dev_llm

    graph = build_graph()
    result = graph.invoke({"raw_input": sample_raw_input})

    assert "user_stories" in result
    assert "code_changes" in result
