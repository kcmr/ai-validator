import shutil
import sys
from pathlib import Path

from agents.validator import run_sync


def _main_sync(prompt: str):
    run_sync(prompt)


def _clean_report_folder() -> None:
    """Clean the playwright-report folder before execution."""
    report_path = Path(__file__).parent.parent.parent / "playwright-report"
    if report_path.exists():
        shutil.rmtree(report_path)


def main() -> None:
    """Synchronous entry point for console script.

    Wraps the async implementation so `[project.scripts]` can call it.
    """
    # Clean report folder before execution
    _clean_report_folder()

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
