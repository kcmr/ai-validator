from config.settings import settings
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.github import GitHubProvider

github_model = OpenAIChatModel(
    settings.llm_model_name,
    provider=GitHubProvider(api_key=settings.llm_api_key),
)
