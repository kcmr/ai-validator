from pydantic_ai.models.google import GoogleModel
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.github import GitHubProvider
from pydantic_ai.providers.google import GoogleProvider
from pydantic_ai.providers.ollama import OllamaProvider
from pydantic_ai.providers.openai import OpenAIProvider

from config.settings import settings

_ollama_provider = OllamaProvider(base_url="http://localhost:11434/v1")

models: dict[str, OpenAIChatModel | GoogleModel] = {
    "github": OpenAIChatModel(
        settings.llm_model_name,
        provider=GitHubProvider(api_key=settings.llm_api_key),
    ),
    "openai": OpenAIChatModel(
        "gpt-4o",
        provider=OpenAIProvider(api_key=settings.llm_api_key),
    ),
    "gemini": GoogleModel(
        model_name="gemini-2.5-flash",
        provider=GoogleProvider(api_key=settings.llm_api_key),
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
