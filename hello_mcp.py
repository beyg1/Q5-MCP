from mcp.server.fastmcp import FastMCP
from mcp.types import TextContent

mcp = FastMCP(
    name = "ALi Mcp Server",
    stateless_http = True,
)

mcp_app = mcp.streamable_http_app()