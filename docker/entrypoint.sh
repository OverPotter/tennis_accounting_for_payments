#!/bin/bash
set -e

alembic upgrade head
python src/tg_main.py
