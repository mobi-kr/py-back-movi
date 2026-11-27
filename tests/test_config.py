import pytest

from app.core.config import Settings


def test_settings_defaults(monkeypatch: pytest.MonkeyPatch) -> None:
    for key in ("APP_NAME", "APP_ENV", "DEBUG", "LOG_LEVEL"):
        monkeypatch.delenv(key, raising=False)

    settings = Settings(_env_file=None)

    assert settings.app_name == "py-back-movi"
    assert settings.app_env == "local"
    assert settings.debug is False
    assert settings.log_level == "INFO"


def test_settings_from_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("APP_ENV", "test")
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")

    settings = Settings(_env_file=None)

    assert settings.app_env == "test"
    assert settings.log_level == "DEBUG"
