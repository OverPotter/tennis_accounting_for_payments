#!/bin/bash
set -e

alembic upgrade head
exec watchmedo auto-restart --directory=./src --pattern="*.py" --recursive -- python src/tg_main.py
