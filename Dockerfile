FROM ghcr.io/astral-sh/uv:debian-slim

WORKDIR /app

# Enable bytecode compilation and set the environment path
ENV UV_COMPILE_BYTECODE=1
ENV PATH="/app/.venv/bin:$PATH"

COPY pyproject.toml uv.lock /app/

# Install dependencies without the project itself for better caching
RUN uv sync --frozen --no-install-project

COPY . /app

EXPOSE 8000

# Use --host 0.0.0.0 to allow external connections
CMD ["uv", "run", "fastapi", "dev", "main.py", "--host", "0.0.0.0", "--port", "8000"]



# FROM ghcr.io/astral-sh/uv:debian-slim

# WORKDIR /app

# COPY pyproject.toml uv.lock /app/

# RUN uv sync --locked    

# COPY . /app

# EXPOSE 8000

# CMD ["uv", "run", "fastapi", "dev", "main.py", "--host", "0.0.0.0", "--port", "8000"]
