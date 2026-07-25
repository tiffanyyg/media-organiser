from app.config.settings import load_settings


def test_settings_load():
    settings = load_settings()

    assert "library" in settings
    assert "storage" in settings

