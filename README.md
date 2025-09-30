# AI Validator

Sistema de validación automática de flujos web que combina una aplicación Next.js con un agente de IA para automatizar pruebas de interfaz de usuario.

## Requisitos

- Node.js v22 (usar nvm: `nvm install && nvm use`)
- Python 3.13+
- [uv](https://docs.astral.sh/uv/) para gestión de dependencias Python

## Configuración

### Aplicación web

```bash
cd web
nvm use
npm ci
npm run dev
```

La aplicación estará disponible en `http://localhost:3000`

### Agente de validación

```bash
cd agent
uv sync
uv run ai-validator-agent
```

El agente validará automáticamente las instrucciones especificadas en el prompt de usuario proporcionado.
