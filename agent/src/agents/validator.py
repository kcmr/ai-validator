from pathlib import Path
from typing import Literal

from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.mcp import load_mcp_servers

from llm_models import open_ai_model

# Get the project root directory
project_root = Path(__file__).parent.parent.parent
mcp_file_path = project_root / "mcp.json"

servers = load_mcp_servers(str(mcp_file_path))
print(f"Loaded {len(servers)} servers from {mcp_file_path}")


class ResponseModel(BaseModel):
    status: Literal["success", "failure"]
    details: str


agent = Agent(
    model=open_ai_model,
    system_prompt="""
        <system>
        You are an AI agent specialized in functional testing of web applications.
        
        Your task is to validate the proper functioning of a web application by 
        performing a series of tests based on the provided user prompt.

        To do so, you are provided with a set of tools that allow you to interact with 
        the web application. You can use these tools to navigate through the 
        application, fill out forms, click buttons, and verify that the expected 
        outcomes are achieved.
        </system>

        <output>
        Return a concise summary of the results of your tests in markdown format and
        the status of the tests as "success" or "failure". If any test fails, 
        consider the overall status as "failure".
        </output>
        """,
    output_type=ResponseModel,
    toolsets=servers,
    model_settings={
        # "temperature": 0.2,
        "timeout": 300.0,
    },
)


def run_sync(user_prompt: str):
    response = agent.run_sync(user_prompt)
    if isinstance(response.output, str):
        print(response.output)
    else:
        print(response.output.model_dump_json(indent=2))


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
