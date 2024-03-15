from functools import lru_cache

from .config_model import Settings


@lru_cache()
def get_settings():
    return Settings(_env_file=".env")
