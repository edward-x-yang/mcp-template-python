<h1 align="center">MCP Template Python</h1>

A simple template implementation of the [Model Context Protocol (MCP)](https://modelcontextprotocol.io) server that contains a basic tool returning a secret phrase. 

Use this as a reference point to build your MCP servers yourself, or give this as an example to an AI coding assistant and tell it to follow this example for structure and code correctness!

## Overview

This project demonstrates how to build a basic MCP server using FastMCP. It serves as a practical template for creating your own MCP servers with minimal setup.

The implementation follows the best practices laid out by Anthropic for building MCP servers, allowing seamless integration with any MCP-compatible client.

## Features

The server provides a simple test tool:

1. **`secret_phrase`**: Returns a test secret phrase for verification

## Prerequisites

- Python 3.12+
- uv (Python package manager)
- ngrok (for tunneling local servers)

## Installation

### Using uv

1. Install uv if you don't have it:
   ```bash
   pip install uv
   ```

2. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd mcp-template-python
   ```

3. Install dependencies:
   ```bash
   uv sync
   ```

### Using Docker (Optional)

1. Build the Docker image:
   ```bash
   docker build -t mcp-template-python --build-arg PORT=8050 .
   ```

2. Create a `.env` file and configure your environment variables

## Configuration

The following environment variables can be configured in your `.env` file:

| Variable | Description | Default |
|----------|-------------|---------|
| `TRANSPORT` | Transport protocol (sse or stdio) | `sse` |
| `HOST` | Host to bind to when using SSE transport | `0.0.0.0` |
| `PORT` | Port to listen on when using SSE transport | `8050` |

## Running the Server

### Local Development

#### SSE Transport

```bash
uv run src/main.py
```

The MCP server will run as an API endpoint on `http://localhost:8050`.

#### Stdio Transport

With stdio, the MCP client itself can spin up the MCP server, so no need to run it manually.

### Using Docker

#### SSE Transport

```bash
docker run --env-file .env -p 8050:8050 mcp-template-python
```

#### Stdio Transport

With stdio, the MCP client itself can spin up the MCP server container.

## Tunneling with ngrok

To make your local MCP server accessible over the internet (useful for testing with cloud-based MCP clients):

### Setup ngrok

1. Sign up at [ngrok.com](https://ngrok.com) and get your auth token
2. Install ngrok:
   ```bash
   brew install ngrok  # macOS
   # or download from https://ngrok.com/download
   ```
3. Configure ngrok:
   ```bash
   ngrok config add-authtoken YOUR_AUTH_TOKEN
   ```

### Create a Static Domain (Recommended)

1. Get a free static domain from your ngrok dashboard
2. Start your MCP server:
   ```bash
   uv run src/main.py
   ```
3. In another terminal, start the tunnel with the skip-browser-warning header:
   ```bash
   ngrok http --url=wondrous-turtle-polite.ngrok-free.app --request-header-add="ngrok-skip-browser-warning:true" 8050
   ```

Your MCP server will now be accessible at `https://your-static-domain.ngrok-free.app`

### Using Ephemeral Domain

If you prefer not to use a static domain:

```bash
ngrok http --request-header-add="ngrok-skip-browser-warning:true" 8050
```

This will give you a temporary URL that changes each time you restart ngrok.

## Integration with MCP Clients

### SSE Configuration

#### Local Server
For a local server running on localhost:

```json
{
  "mcpServers": {
    "mcp-template-python": {
      "transport": "sse",
      "url": "http://localhost:8050/sse"
    }
  }
}
```

#### Tunneled Server
For a server accessible via ngrok tunnel:

```json
{
  "mcpServers": {
    "mcp-template-python": {
      "transport": "sse",
      "url": "https://your-static-domain.ngrok-free.app/sse"
    }
  }
}
```

> **Note for Windsurf users**: Use `serverUrl` instead of `url` in your configuration.

### Stdio Configuration

#### Using uv

```json
{
  "mcpServers": {
    "mcp-template-python": {
      "command": "uv",
      "args": ["run", "src/main.py"],
      "cwd": "/path/to/mcp-template-python",
      "env": {
        "TRANSPORT": "stdio"
      }
    }
  }
}
```

#### Using Docker

```json
{
  "mcpServers": {
    "mcp-template-python": {
      "command": "docker",
      "args": ["run", "--rm", "-i", "-e", "TRANSPORT=stdio", "mcp-template-python"]
    }
  }
}
```

## Building Your Own Server

This template provides a foundation for building more complex MCP servers. To build your own:

1. Add your own tools by creating methods with the `@mcp.tool()` decorator
2. Modify the server configuration as needed
3. Add any additional dependencies to `pyproject.toml`
4. Feel free to add prompts and resources as well with `@mcp.resource()` and `@mcp.prompt()`
