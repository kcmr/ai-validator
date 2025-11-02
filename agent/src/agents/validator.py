import json
from collections.abc import Sequence
from pathlib import Path

import logfire
from pydantic_ai import AbstractToolset, Agent, ToolsetFunc
from pydantic_ai.mcp import load_mcp_servers

from llm_models import models
from models import ResponseModel
from prompts import functional_testing_prompt
from utils import log_stream

logfire.configure()
logfire.instrument_pydantic_ai()

REPORTS_DIR = Path("reports")


def get_tools() -> Sequence[AbstractToolset[None] | ToolsetFunc[None]] | None:
    project_root = Path(__file__).parent.parent.parent
    mcp_file_path = project_root / "mcp.json"

    mcp_servers = load_mcp_servers(str(mcp_file_path))
    print(f"Loaded {len(mcp_servers)} servers from {mcp_file_path}")

    return mcp_servers


def save_message_logs(agent_run):
    REPORTS_DIR.mkdir(exist_ok=True)

    if agent_run and agent_run.result is not None:
        with open(REPORTS_DIR / "agent_run_result.json", "wb") as f:
            f.write(agent_run.result.all_messages_json())


def save_result(result: ResponseModel) -> None:
    """Save the final validation result to result.json."""
    REPORTS_DIR.mkdir(exist_ok=True)

    if result is not None:
        with open(REPORTS_DIR / "result.json", "w") as f:
            json.dump(result.model_dump(), f, indent=2, ensure_ascii=False)


agent = Agent(
    name="Validator Agent",
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
            log_stream(node)

    if agent_run and agent_run.result is not None:
        save_message_logs(agent_run)
        save_result(agent_run.result.output)
