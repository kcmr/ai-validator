from pathlib import Path

from pydantic_ai import Agent
from pydantic_ai.mcp import load_mcp_servers

from llm_models import github_model

# Get the project root directory
project_root = Path(__file__).parent.parent.parent
mcp_file_path = project_root / "mcp.json"

servers = load_mcp_servers(str(mcp_file_path))
print(f"Loaded {len(servers)} servers from {mcp_file_path}")

agent = Agent(
    model=github_model,
    system_prompt="""
        You are an AI agent specialized in functional testing of web applications.
        
        Your task is to validate the proper functioning of a web application by 
        performing a series of tests based on the provided user prompt.

        To do so, you are provided with a set of tools that allow you to interact with 
        the web application. You can use these tools to navigate through the 
        application, fill out forms, click buttons, and verify that the expected 
        outcomes are achieved.

        Return a concise summary of the results of your tests in markdown format.
        """,
    toolsets=servers,
)


def run_sync(user_prompt: str):
    response = agent.run_sync(user_prompt)
    print(response.output)


async def run_stream():
    async with agent.run_stream(
        "Navega a http://localhost:3000 y comprueba que se pueden introducir datos en "
        "el formulario y enviarlos."
    ) as response:
        async for text in response.stream_text():
            print(text)


async def iter():
    nodes = []
    async with agent.iter("¿Cuál es la capital de Francia?") as agent_run:
        async for node in agent_run:
            nodes.append(node)

    print(nodes)
