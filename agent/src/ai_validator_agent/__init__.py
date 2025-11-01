import asyncio
import shutil
from pathlib import Path
from typing import Annotated

import typer

from agents.validator import run
from prompts import simple_user_prompt

app = typer.Typer(help="AI Validator Agent - Validate web applications with AI")


def _clean_report_folder() -> None:
    """Clean the playwright-report folder before execution."""
    report_path = Path(__file__).parent.parent.parent / "playwright-report"
    if report_path.exists():
        shutil.rmtree(report_path)


@app.command()
def validate(
    file: Annotated[
        Path | None,
        typer.Option(
            "--file",
            "-f",
            help="Path to markdown file containing the validation prompt",
            exists=True,
            file_okay=True,
            dir_okay=False,
            readable=True,
        ),
    ] = None,
    text: Annotated[
        str | None,
        typer.Option(
            "--text",
            "-t",
            help="Direct text prompt for validation",
        ),
    ] = None,
) -> None:
    """
    Run the AI validator with either a markdown file or direct text input.

    If neither --file nor --text is provided, the default prompt will be used.
    If both are provided, --file takes precedence.
    """
    # Clean report folder before execution
    _clean_report_folder()

    # Determine which prompt to use
    if file:
        typer.echo(f"Reading prompt from file: {file}")
        prompt = file.read_text(encoding="utf-8")
    elif text:
        typer.echo("Using provided text prompt")
        prompt = text
    else:
        typer.echo("No prompt provided. Using default prompt.")
        prompt = simple_user_prompt

    # Run the validator
    asyncio.run(run(prompt))


def main() -> None:
    """Synchronous entry point for console script.

    Wraps the Typer app so `[project.scripts]` can call it.
    """
    app()


if __name__ == "__main__":
    main()
