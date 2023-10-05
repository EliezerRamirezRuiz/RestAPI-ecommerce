from typing import TypedDict


class DefaultConfig(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'secret'


class DevelopmentConfig(DefaultConfig):
    DEBUG = True


class ProductionConfig(DefaultConfig):
    SECRET_KEY = 'eueueueueueueeuueueue'
    

class DictConfig(TypedDict):
    default: DefaultConfig
    development: DevelopmentConfig
    production: ProductionConfig
    

def setup_config(mode:str) -> object:
    return DictConfig().get(mode, 'default')
