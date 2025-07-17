from mcp.server.fastmcp import FastMCP, Context
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

# Initialize FastMCP server with minimal configuration
mcp = FastMCP(
    "mcp-template-python",
    description="Minimal MCP server template with test functionality",
    host=os.getenv("HOST", "0.0.0.0"),
    port=int(os.getenv("PORT", "8050"))
)

@mcp.tool()
async def secret_phrase(ctx: Context) -> str:
    """Returns a secret phrase.

    This tool returns a simple secret phrase for testing purposes.
    """
    return "I love pizza!"

async def main():
    transport = os.getenv("TRANSPORT", "sse")
    if transport == 'sse':
        # Run the MCP server with sse transport
        await mcp.run_sse_async()
    else:
        # Run the MCP server with stdio transport
        await mcp.run_stdio_async()

if __name__ == "__main__":
    asyncio.run(main())
