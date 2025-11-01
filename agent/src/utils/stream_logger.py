from typing import Any

from pydantic_ai._agent_graph import CallToolsNode, ModelRequestNode, UserPromptNode
from pydantic_graph import End
from rich.console import Console

console = Console()


def log_stream(node: Any) -> None:
    """Log the agent event stream node."""
    if isinstance(node, UserPromptNode):
        _log_user_prompt(node)
    elif isinstance(node, ModelRequestNode):
        _log_model_request()
    elif isinstance(node, CallToolsNode):
        _log_call_tools(node)
    elif isinstance(node, End):
        _log_end()


def _log_user_prompt(node: Any) -> None:
    """Log user prompt node."""
    user_prompt = node.user_prompt
    if isinstance(user_prompt, str):
        preview = user_prompt[:100] if len(user_prompt) > 100 else user_prompt
        console.print(f"[bold blue]📝 User Prompt:[/bold blue] [dim]{preview}...[/dim]")


def _log_model_request() -> None:
    """Log model request node."""
    console.print(
        "[bold yellow]💭 Thinking...[/bold yellow] "
        "[dim]Model is processing request[/dim]"
    )


def _log_call_tools(node: Any) -> None:
    """Log call tools node."""
    if not hasattr(node, "model_response") or not node.model_response:
        return

    if not hasattr(node.model_response, "parts"):
        return

    for part in node.model_response.parts:
        part_type = type(part).__name__
        tool_name = getattr(part, "tool_name", "unknown")

        if "ToolCall" in part_type:
            console.print(
                f"[bold magenta]🔧 Tool calling request[/bold magenta] "
                f"Calling tool: [cyan]{tool_name}[/cyan]"
            )
        elif "ToolReturn" in part_type:
            console.print(
                f"[bold green]✅ Tool calling response[/bold green] "
                f"Tool '[cyan]{tool_name}[/cyan]' completed"
            )


def _log_end() -> None:
    """Log end node."""
    console.print("[bold green]🏁 Execution completed[/bold green]")
