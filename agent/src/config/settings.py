from pydantic import Field, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    llm_model_name: str = Field(default="your-model-name")
    llm_api_key: str = Field(default="your-api-key")
    logfire_token: str = Field(default="your-logfire-token")

    model_config = SettingsConfigDict(env_file=".env")


try:
    settings = Settings()
except ValidationError as e:
    print("Error loading settings:", e)
    raise
