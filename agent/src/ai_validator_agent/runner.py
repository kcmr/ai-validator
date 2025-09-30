from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from pydantic_ai import Agent

DEFAULT_SYSTEM_PROMPT = (
    "Eres un agente QA que valida flujos funcionales en una web de demostración. "
    "Usa Playwright a través del MCP cuando necesites interactuar con el navegador."
)


@dataclass
class AgentConfig:
    """Parámetros mínimos para inicializar el agente."""

    model: str = "gpt-4o-mini"
    system_prompt: str = DEFAULT_SYSTEM_PROMPT
    mcp_endpoint: Optional[str] = None


def _bootstrap_mcp(endpoint: Optional[str]) -> None:
    """Conecta con el servidor MCP de Playwright.

    Placeholder: cuando Playwright MCP esté disponible abriremos la conexión aquí
    (por ejemplo usando `mcp.client.stdio`).
    """

    if endpoint:
        raise NotImplementedError("Integración MCP pendiente de implementar")


def build_agent(config: Optional[AgentConfig] = None) -> Agent:
    """Crea una instancia del agente con la configuración indicada."""

    cfg = config or AgentConfig()

    # Aquí se registrarán herramientas MCP en siguientes iteraciones.
    agent = Agent(model=cfg.model, system_prompt=cfg.system_prompt)
    return agent


def run_agent(prompt: str, config: Optional[AgentConfig] = None) -> str:
    """Ejecuta el agente con el prompt proporcionado y devuelve la respuesta básica."""

    cfg = config or AgentConfig()
    _bootstrap_mcp(cfg.mcp_endpoint)

    agent = build_agent(cfg)
    result = agent.run(prompt)

    return getattr(result, "output_text", str(result))
