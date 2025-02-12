FROM python:3.10.0-slim

WORKDIR /app
ENV PYTHONPATH=/app
ENV LANG=ru_RU.UTF-8 \
    LANGUAGE=ru_RU:ru \
    LC_ALL=ru_RU.UTF-8

RUN apt-get update && \
    apt-get install -y --no-install-recommends locales && \
    echo "ru_RU.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen && \
    apt-get purge -y --auto-remove && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --no-dev

COPY src ./src
COPY alembic.ini ./alembic.ini

CMD ["python", "src/tg_main.py"]
