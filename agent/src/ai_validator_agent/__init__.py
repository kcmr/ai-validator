import asyncio

from agents.validator import agent, run_sync

user_prompt = (
    "Navega a http://localhost:3000 e introduce 'fake_user' en el campo de "
    "usuario y 'fake_password' en el campo de contraseña y envía el formulario."
    "Verifica que la respuesta contiene 'Credenciales recibidas' e incluye "
    "el nombre de usuario introducido."
)


def _main_sync():
    run_sync(user_prompt)


async def _main_async():
    await agent.to_cli()


def main() -> None:
    """Synchronous entry point for console script.

    Wraps the async implementation so `[project.scripts]` can call it.
    """
    # asyncio.run(_main_async())
    _main_sync()
