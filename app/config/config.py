import os

class Config:
    CONNECTION_STRING = os.getenv("CONNECTION_STRING", "default_connection_string")
    OTEL_SERVICE_NAME = "MyFlaskApp"  

class DevelopmentConfig(Config):
    DEBUG = True
    OTEL_SERVICE_NAME = "MyFlaskApp-Dev"

class ProductionConfig(Config):
    DEBUG = False
    OTEL_SERVICE_NAME = "MyFlaskApp-Prod"

def factory(config_name):
    if config_name == 'production':
        return ProductionConfig
    return DevelopmentConfig
