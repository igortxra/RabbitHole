FROM python:3.13-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

ADD ./pyproject.toml ./uv.lock ./worker.py /app

RUN uv sync --frozen
CMD ["uv", "run", "python", "worker.py"]
