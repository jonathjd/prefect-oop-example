# Dockerfile

# Use the official uv runtime as the base image.
FROM astral/uv:0.2-python3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the dependency definition file first to leverage Docker's layer caching.
COPY pyproject.toml .

# Install the project and its dependencies defined in pyproject.toml using uv.
RUN uv pip install --system .

# Copy the rest of your application's source code into the container.
COPY . .

# Set the default command to run your Prefect flow.
CMD ["python", "etl.py"]