import typer

from .runner import AgentConfig, run_agent


def main(
    prompt: str = typer.Option(..., "--prompt", help="Instrucciones en lenguaje natural"),
    model: str = typer.Option("gpt-4o-mini", help="Modelo LLM a utilizar"),
    mcp_endpoint: str | None = typer.Option(
        None,
        help="Endpoint o comando para iniciar el MCP de Playwright (pendiente de implementar)",
    ),
) -> None:
    """Ejecuta el agente con las instrucciones indicadas."""

    cfg = AgentConfig(model=model, mcp_endpoint=mcp_endpoint)
    response = run_agent(prompt, cfg)
    typer.echo(response)


if __name__ == "__main__":
    typer.run(main)
