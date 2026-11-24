default:
    @just --list

setup:
    uv sync --locked

fmt:
    uv run --locked isort src
    uv run --locked ruff format src

lint:
    uv run --locked ruff check --no-fix src
    uv run --locked ruff format --check src
    uv run --locked mypy src

clean:
    rm -rf build dist src/*.egg-info .ruff_cache
    find . -name '__pycache__' -exec rm -rf {} +
