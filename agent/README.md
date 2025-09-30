# Agente de validación

Este módulo contiene el esqueleto de un agente basado en Pydantic AI que se conectará al MCP de Playwright.

```bash
# activando entorno virtual recomendado
python -m venv .venv
source .venv/bin/activate

# instalar dependencias del agente
pip install -e .

# ejecutar agente con un prompt de prueba
python -m ai_validator_agent.run --prompt "Verifica que el formulario se renderiza"
```

La implementación actual solo registra el prompt y produce una respuesta simulada. A medida que se implemente la integración con MCP se añadirán herramientas reales basadas en Playwright.
