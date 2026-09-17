import os
import sys

from mcp import StdioServerParameters

from shared.mcp_client import McpClientBase


class TabletMcpClient(McpClientBase):
    def __init__(self) -> None:
        super().__init__(name="tablet-mcp-client")

        self.server_script = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "server.py"
        )


    def build_server_parameters(self) -> StdioServerParameters:
        return StdioServerParameters(
            command=sys.executable,
            args=[self.server_script],
            env=None,
        )


    async def on_connected(self) -> None:
        tools = await self.list_tools()
        print(f"[{self.name}] spawned its own server. Available tools: {tools}")


    async def open_url(self, url: str) -> str:
        result = await self.call_tool("open_url", {"url": url})
        return self.first_text(result)