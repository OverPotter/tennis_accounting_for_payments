from pathlib import Path

TMP_DIR = Path(__file__).resolve().parents[0] / "tmp"
ENV_PATH = Path(__file__).resolve().parents[1] / "docker" / "backend" / ".env"
