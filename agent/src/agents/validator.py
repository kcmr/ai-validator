import random

from pydantic_ai import Agent

from llm_models import github_model

agent = Agent(
    model=github_model,
    system_prompt="""
        Responde de forma cortante invitando al usuario a buscar por sí mismo.
        Finaliza con un insulto en español.""",
)


@agent.tool_plain
def insulto() -> str:
    """Genera un insulto aleatorio en español."""
    choices = [
        "Cenutrio",
        "Mentecato",
        "Necio",
        "Zopenco",
        "Pedazo de mierda",
        "Palurdo",
        "Tonto del culo",
        "Zoquete",
    ]

    return random.choice(choices)


def run_sync(user_prompt: str):
    response = agent.run_sync(user_prompt)
    print(response.output)


async def run_stream():
    async with agent.run_stream(
        "¿Quién es el presidente de Estados Unidos?"
    ) as response:
        async for text in response.stream_text():
            print(text)


async def iter():
    nodes = []
    async with agent.iter("¿Cuál es la capital de Francia?") as agent_run:
        async for node in agent_run:
            nodes.append(node)

    print(nodes)
