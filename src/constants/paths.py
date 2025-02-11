from pathlib import Path

TMP_DIR = Path(__file__).resolve().parents[1] / "tmp"
ENV_PATH = Path(__file__).resolve().parents[2] / "docker" / "backend" / ".env"
