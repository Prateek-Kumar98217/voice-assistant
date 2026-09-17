from mcp.server import MCPServer

from tablet_agent.actions import open_safe_url


mcp_server = MCPServer(
    name="tablet-tools-server"
)

@mcp_server.tool()
def open_url(url: str):
    return open_safe_url(url)

if __name__=="__main__":
    mcp_server.run(transport="stdio")