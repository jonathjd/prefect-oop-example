# Prefect 3 pipeline example with uv, and Docker
This repository is a template demonstrating how to package a Prefect 3 workflow into a Docker container using `uv` for rapid dependency management. It also uses an OOP based approach to creating flows.

# ✨ Features
**OOP Design**: Uses an OOP design for logic instead of strictly procedural code.

**Fast Builds**: Uses `uv` and a `pyproject.toml` file to install Python dependencies quickly.

**Modern Logging**: Uses `loguru` for modern logging.

**Fast Formatting⚡️**: Uses ruff for formating and linting.

**Containerized**: A Dockerfile that packages the Prefect flow into an image.

**Modern Python**: Follows current best practices for Python project structure.

**Simple Deployment**: Serves a Prefect deployment from a long-lived Docker container.

# 🚀 Getting Started
Follow these steps to build and run the containerized Prefect flow on your local machine.

## Prerequisites
`uv` must be installed along with Docker, and you must have either a Prefect Cloud account or a local Prefect server instance.

1. Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
2. Configure Environment Variables
Create a file named .env in the project's root directory. This file securely provides your Prefect API credentials to the Docker container.

```bash
# .env
PREFECT_API_URL="<YOUR-PREFECT-API-URL>"
PREFECT_API_KEY="<YOUR-PREFECT-API-KEY>"
```
**Note**: Replace the placeholder values with your actual Prefect API URL and API Key. These are not needed if running prefect locally.

3. Build the Docker Image
Use the docker build command to create an image from the Dockerfile. We'll tag it as prefect-uv-example.

```bash
docker build -t prefect-uv-example .
```
4. Run the Docker Container
Run the image as a container in detached mode (-d), which is ideal for a long-running agent.

```bash
docker run -d --name my-prefect-agent --env-file .env prefect-uv-example
```

# ⚙️ Usage
Your Prefect flow is now running and awaiting work from your Prefect workspace.

Verify the Container is Running
To see your active container, run:

```bash
docker ps
```

## View Logs
To see the live output from your flow, including the link to your deployment in the Prefect UI, run:

```bash
docker logs my-prefect-agent
```

## Stop the Container
When you're finished, you can stop the container using its name:

```bash
docker stop my-prefect-agent
```