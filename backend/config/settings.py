"""Centralised application settings loaded from environment / .env."""

from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent / ".env")


class Settings:
    """All runtime config in one place. Read from env vars; fail fast on missing."""

    # Azure OpenAI
    azure_openai_api_key: str = os.environ["AZURE_OPENAI_API_KEY"]
    azure_openai_base_url: str = os.environ["AZURE_OPENAI_BASE_URL"]
    azure_openai_model: str = os.environ["AZURE_OPENAI_MODEL"]

    # LLM behaviour
    llm_temperature: float = float(os.getenv("LLM_TEMPERATURE", "0.2"))

    # Output
    output_dir: Path = Path(__file__).parent.parent / "output"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return the singleton settings instance."""
    return Settings()
