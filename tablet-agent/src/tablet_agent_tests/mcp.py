from tablet_agent.mcp import TabletMcpClient

async def test_client():
    mcp_client = TabletMcpClient()

    async with mcp_client:
        result = await mcp_client.open_url("something.com")
        print(f"MCP tool execution result: {result}")
        result = await mcp_client.open_url("https://something.com")
        print(f"MCP tool execution result: {result}")

    print("MCP subprocess shutdown complete.")