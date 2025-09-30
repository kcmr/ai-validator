import sys

from agents.validator import run_sync


def _main_sync(prompt: str):
    run_sync(prompt)


def main() -> None:
    """Synchronous entry point for console script.

    Wraps the async implementation so `[project.scripts]` can call it.
    """
    # Get the prompt from command line arguments
    if len(sys.argv) < 2:
        default_prompt = (
            "Navega a http://localhost:3000 e introduce 'fake_user' en el campo de "
            "usuario y 'fake_password' en el campo de contraseña y envía el formulario."
            "Verifica que la respuesta contiene 'Credenciales recibidas' e incluye "
            "el nombre de usuario introducido."
        )
        print("No prompt provided. Using default prompt.")
        prompt = default_prompt
    else:
        prompt = " ".join(sys.argv[1:])

    _main_sync(prompt)
