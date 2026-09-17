from abc import ABC
from contextlib import AsyncExitStack
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


class McpClientBase(ABC):
    def __init__(self, name:str)-> None:
        """Base class for an MCP client connected over stdio."""

        self._exit_stack = AsyncExitStack()
        self._connected: bool = False
        self.name: str = name
        self.session: ClientSession | None = None


    def build_server_parameters(self) -> StdioServerParameters:
        """
        Return the StdioServerParameters describing the subprocess to
        launch (command, args, env). Must be implemented by subclasses.
        
        """

        raise NotImplementedError
    

    async def on_connected(self) -> None:
        """
        Hook called right after session.initialize() succeeds.Probably
        for logging.
        """

        pass


    async def connect(self) -> None:
        if self._connected:
            return 

        server_params = self.build_server_parameters()

        read_stream, write_stream = await self._exit_stack.enter_async_context(
            stdio_client(server_params)
        )

        self.session = await self._exit_stack.enter_async_context(
            ClientSession(read_stream, write_stream)
        )

        await self.session.initialize()
        self._connected = True
        await self.on_connected()


    async def close(self):
        await self._exit_stack.aclose()
        self._connected = False
        self.session = None


    async def __aenter__(self) -> "McpClientBase":
        await self.connect()
        return self


    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self.close()


    def _require_session(self) -> ClientSession:
        if self.session is None:
            raise RuntimeError(f"{self.name}: not connected. Call connect() first.")
        return self.session
    

    async def list_tools(self) -> list[str]:
        result = await self._require_session().list_tools()
        return [tool.name for tool in result.tools]


    async def call_tool(self, tool_name: str, arguments: dict | None = None):
        return await self._require_session().call_tool(tool_name, arguments or {})


    async def list_resources(self) -> list[str]:
        result = await self._require_session().list_resources()
        return [str(resource.uri) for resource in result.resources] 


    @staticmethod
    def first_text(call_tool_result) -> str:
        """Convenience: pull the plain-text payload out of a call_tool result."""
        
        for block in call_tool_result.content:
            if getattr(block, "type", None) == "text":
                return block.text
        return str(call_tool_result)