import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv(override=True)


class ReservoirSettings(BaseSettings):
    # model_config = SettingsConfigDict(env_prefix="reservoir_")

    api_key: str = os.getenv("RESERVOIR_API_KEY")


class OpenAISettings(BaseSettings):
    # model_config = SettingsConfigDict(env_prefix="openai_")

    api_key: str = os.getenv("OPENAI_API_KEY")


class Settings(BaseSettings):
    db_path: str = "sample.db"
    reservoir: ReservoirSettings = ReservoirSettings()
    openai: OpenAISettings = OpenAISettings()
