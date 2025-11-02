from httpx import AsyncClient
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.github import GitHubProvider
from pydantic_ai.providers.google import GoogleProvider
from pydantic_ai.providers.ollama import OllamaProvider
from pydantic_ai.providers.openai import OpenAIProvider

from config.settings import settings
from utils import create_retrying_client

_retrying_client: AsyncClient | None = None


def get_retrying_client() -> AsyncClient:
    global _retrying_client
    if _retrying_client is None:
        _retrying_client = create_retrying_client(mode="standard")
    return _retrying_client


_ollama_provider = OllamaProvider(base_url="http://localhost:11434/v1")

models: dict[str, OpenAIChatModel | GoogleModel] = {
    "github": OpenAIChatModel(
        settings.llm_model_name,
        provider=GitHubProvider(
            api_key=settings.llm_api_key,
            http_client=get_retrying_client(),
        ),
    ),
    "openai": OpenAIChatModel(
        "gpt-4o",
        provider=OpenAIProvider(
            api_key=settings.llm_api_key,
            http_client=get_retrying_client(),
        ),
    ),
    "gemini": GoogleModel(
        model_name="gemini-2.5-flash",
        provider=GoogleProvider(
            api_key=settings.llm_api_key,
            http_client=get_retrying_client(),
        ),
    ),
    "ollama_mistral": OpenAIChatModel(
        model_name="mistral:7b-instruct",
        provider=_ollama_provider,
    ),
    "ollama_llama": OpenAIChatModel(
        model_name="llama3.1:8b",
        provider=_ollama_provider,
    ),
    # Does not support tool function calling
    "ollama_deepseek": OpenAIChatModel(
        model_name="deepseek-r1:8b",
        provider=_ollama_provider,
    ),
    "ollama_qwen": OpenAIChatModel(
        model_name="qwen2.5:7b-instruct",
        provider=_ollama_provider,
    ),
}
