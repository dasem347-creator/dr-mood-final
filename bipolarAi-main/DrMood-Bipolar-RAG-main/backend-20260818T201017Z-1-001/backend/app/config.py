from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    gemini_api_key: str = ""
    llm_model: str = "gemini-3.6-flash"
    jwt_secret: str = "change-this-development-secret"
    jwt_algorithm: str = "HS256"
    jwt_expire_minutes: int = 60 * 24
    google_client_id: str = ""

    database_url: str = "sqlite:///./drmood.db"
    chroma_persist_dir: str = "./chroma_store"
    chroma_collection: str = "clinical_sources"
    embedding_model: str = "all-MiniLM-L6-v2"
    retrieval_top_k: int = 4
    retrieval_min_score: float = 0.35
    cors_origins: str = (
        "http://localhost:5500,http://127.0.0.1:5500,"
        "http://localhost:5501,http://127.0.0.1:5501"
    )

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def cors_origin_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()