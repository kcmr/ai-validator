import asyncio
import shutil
import sys
from pathlib import Path

from agents.validator import run
from prompts import simple_user_prompt


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
        default_prompt = simple_user_prompt
        print("No prompt provided. Using default prompt.")
        prompt = default_prompt
    else:
        prompt = " ".join(sys.argv[1:])

    asyncio.run(run(prompt))


if __name__ == "__main__":
    main()
