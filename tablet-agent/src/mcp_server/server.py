from mcp.server import MCPServer

from tablet_agent.actions import open_safe_url


tools_server = MCPServer(
    name="tablet-tools-server"
)

@tools_server.tool()
def open_url(url: str):
    return open_safe_url(url)