import asyncio

from agents.validator import agent, run_sync

user_prompt = (
    "Navega a http://localhost:3000 y comprueba que se pueden introducir "
    "datos en el formulario y enviarlos."
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
