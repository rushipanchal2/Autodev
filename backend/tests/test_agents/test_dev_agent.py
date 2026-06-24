"""Unit tests for the Dev agent."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from graph.agents.dev_agent import dev_agent
from graph.state import CodeChanges, CodeFile


@pytest.fixture()
def mock_code_changes():
    return CodeChanges(
        files=[
            CodeFile(path="app/main.py", content="print('hello')"),
            CodeFile(path="README.md", content="# TODO App"),
        ]
    )


@patch("graph.agents.dev_agent.get_model")
def test_dev_agent_returns_code_changes(mock_get_model, mock_code_changes, sample_user_stories):
    mock_llm = MagicMock()
    mock_llm.with_structured_output.return_value.invoke.return_value = mock_code_changes
    mock_get_model.return_value = mock_llm

    result = dev_agent({"user_stories": sample_user_stories})

    assert "code_changes" in result
    assert "app/main.py" in result["code_changes"]
    assert "README.md" in result["code_changes"]


@patch("graph.agents.dev_agent.get_model")
def test_dev_agent_maps_path_to_content(mock_get_model, mock_code_changes, sample_user_stories):
    mock_llm = MagicMock()
    mock_llm.with_structured_output.return_value.invoke.return_value = mock_code_changes
    mock_get_model.return_value = mock_llm

    result = dev_agent({"user_stories": sample_user_stories})

    assert result["code_changes"]["app/main.py"] == "print('hello')"
