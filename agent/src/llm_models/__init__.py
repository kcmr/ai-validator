from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.github import GitHubProvider
from pydantic_ai.providers.openai import OpenAIProvider

from config.settings import settings

github_model = OpenAIChatModel(
    settings.llm_model_name,
    provider=GitHubProvider(api_key=settings.llm_api_key),
)

open_ai_model = OpenAIChatModel(
    "gpt-4o",
    provider=OpenAIProvider(api_key=settings.llm_api_key),
)
