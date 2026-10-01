from __future__ import annotations

import os

os.environ["DATABASE_URL"] = "sqlite:///./fitbuddy_test.db"
os.environ["DEMO_MODE"] = "true"
os.environ["ALLOW_AI_FALLBACK"] = "true"
os.environ.pop("GEMINI_API_KEY", None)

import pytest
from fastapi.testclient import TestClient

from app.database import Base, engine
from app.main import app


@pytest.fixture(autouse=True)
def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client
