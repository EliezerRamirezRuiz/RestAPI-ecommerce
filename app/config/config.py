from typing import TypedDict


class DefaultConfig(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "secret"
    JWT_SECRET_KEY = "ABCDEFGHIJK"
    SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"


class DevelopmentConfig(DefaultConfig):
    DEBUG = True


class ProductionConfig(DefaultConfig):
    SECRET_KEY = 'eueueueueueueeuueueue'


class DictConfig(TypedDict):
    default: DefaultConfig
    development: DevelopmentConfig 
    production: ProductionConfig


class Config():
    def __init__(self) -> None:
        self.config: DictConfig = {
            "default": DefaultConfig,
            "development": DevelopmentConfig,
            "production": ProductionConfig
        }

    def setup_config(self, mode: str) -> object:
        return self.config.get(mode, 'default')
