"""Application configuration loaded from environment variables."""

from __future__ import annotations

import os
from functools import lru_cache
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

try:
    from dotenv import load_dotenv

    load_dotenv(BASE_DIR / ".env")
except ImportError:
    # The app still works when python-dotenv is not installed and variables are
    # supplied by the operating system.
    pass


def _as_bool(value: str | None, default: bool = False) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


class Settings:
    """Small dependency-free settings object."""

    def __init__(self) -> None:
        self.app_name = os.getenv("APP_NAME", "FitBuddy AI")
        self.app_version = os.getenv("APP_VERSION", "1.0.0")
        self.database_url = os.getenv(
            "DATABASE_URL", f"sqlite:///{BASE_DIR / 'fitbuddy.db'}"
        )
        self.gemini_api_key = os.getenv("GEMINI_API_KEY", "").strip()
        self.gemini_model = os.getenv("GEMINI_MODEL", "gemini-3.8-flash").strip()
        self.demo_mode = _as_bool(os.getenv("DEMO_MODE"), default=False)
        self.allow_ai_fallback = _as_bool(
            os.getenv("ALLOW_AI_FALLBACK"), default=True
        )

    @property
    def ai_enabled(self) -> bool:
        return bool(self.gemini_api_key) and not self.demo_mode


@lru_cache
def get_settings() -> Settings:
    return Settings()
