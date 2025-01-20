#!/bin/bash
alembic upgrade head
python src/tg_main.py
