from pathlib import Path
import tomllib


BASE_DIR = Path(__file__).resolve().parents[2]


def load_settings():
    config_file = BASE_DIR / "config" / "settings.toml"

    with open(config_file, "rb") as file:
        return tomllib.load(file)

