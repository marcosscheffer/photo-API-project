import os

class Config():
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-key")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt-key-dev")
    JWT_ACCESS_TOKEN_EXPIRES = 60 * 15 # 15 minutes
    JWT_REFRESH_TOKEN_EXPIRES = 60 * 60 * 24 * 30 # 30 days

class DevConfig(Config):
    DEBUG=True

config_map = {
    "development": DevConfig,
    "default": DevConfig
}