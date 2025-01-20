FROM python:3.10.0-slim

WORKDIR /app
ENV PYTHONPATH=/app

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

COPY --chmod=777 system/entrypoint.sh /usr/local/bin/entrypoint

COPY src ./src

COPY alembic.ini ./alembic.ini

ENTRYPOINT ["entrypoint"]
