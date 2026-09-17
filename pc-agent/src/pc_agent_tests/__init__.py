import asyncio

from pc_agent_tests.mcp import test_client


def main():
    asyncio.run(test_client())