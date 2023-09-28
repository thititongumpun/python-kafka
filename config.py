from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    broker: str

    model_config = SettingsConfigDict(env_file=".env")
