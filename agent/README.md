# Agente de validación

Este módulo contiene el esqueleto de un agente basado en Pydantic AI que se conectará al MCP de Playwright.

```bash
# crear y activar el entorno con uv
uv venv
source .venv/bin/activate

# instalar dependencias declaradas en pyproject.toml
uv pip install -e .
# (opcional) instalar utilidades de desarrollo
uv pip install pytest>=8.2

# ejecutar el agente con un prompt de prueba
python -m ai_validator_agent.run "Verifica que el formulario se renderiza"
# o, usando uv run
uv run ai-validator-agent "Verifica que el formulario se renderiza"
# o mediante variables de entorno
AI_VALIDATOR_PROMPT="Verifica ..." python -m ai_validator_agent.run
```

La implementación actual solo registra el prompt y produce una respuesta simulada. A medida que se implemente la integración con MCP se añadirán herramientas reales basadas en Playwright.
