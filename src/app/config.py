# src/app/config.py

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    LINE_CHANNEL_SECRET: str
    LINE_CHANNEL_ACCESS_TOKEN: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8" # 建議加上，避免編碼問題

# 建立一個全域可用的設定實例
settings = Settings()