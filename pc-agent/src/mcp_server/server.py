from mcp.server import MCPServer

from pc_agent.actions import open_safe_url


tools_server = MCPServer(
    name="pc-tools-server"
)

@tools_server.tool()
def open_url(url: str):
    return open_safe_url(url)