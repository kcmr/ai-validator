from collections.abc import Sequence
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field
from pydantic_ai import AbstractToolset, Agent, ToolsetFunc
from pydantic_ai.mcp import load_mcp_servers

from llm_models import models
from prompts import functional_testing_prompt


def get_tools() -> Sequence[AbstractToolset[None] | ToolsetFunc[None]] | None:
    project_root = Path(__file__).parent.parent.parent
    mcp_file_path = project_root / "mcp.json"

    mcp_servers = load_mcp_servers(str(mcp_file_path))
    print(f"Loaded {len(mcp_servers)} servers from {mcp_file_path}")

    return mcp_servers


class ResponseModel(BaseModel):
    status: Literal["success", "failure"]
    details: str = Field(..., description="Concise summary of the test results")


agent = Agent(
    model=models["gemini"],
    instructions=functional_testing_prompt,
    output_type=ResponseModel,
    toolsets=get_tools(),
    retries=5,
)


async def run(user_prompt: str):
    nodes: list = []
    agent_run = None
    async with agent.iter(user_prompt) as agent_event:
        agent_run = agent_event
        async for node in agent_run:
            nodes.append(node)
            print(node)

    if agent_run and agent_run.result is not None:
        with open("reports/agent_run_result.json", "wb") as f:
            f.write(agent_run.result.all_messages_json())
