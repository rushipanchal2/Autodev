from __future__ import annotations

from langchain_openai import ChatOpenAI

from config.settings import get_settings


def get_model() -> ChatOpenAI:
    """Return the shared chat model for all agents."""
    s = get_settings()
    return ChatOpenAI(
        base_url=s.azure_openai_base_url,
        api_key=s.azure_openai_api_key,
        model=s.azure_openai_model,
        temperature=s.llm_temperature,
    )
