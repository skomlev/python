"""Aplication Settigs."""
import os


class BaseConfig:
    """Base configuration for all deploy contexts."""

    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    APP_HOST = "127.0.0.1"
    APP_PORT = 5000
    SECRET_KEY = "SECRET_KEY"
    STATIC_DIR = "/static"
    TEMPLATE_DIR = "/templates"
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "postgres://user:123456789@db:5432/bkr_db"


class ProductionConfig(BaseConfig):
    """Production configuration."""

    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = ""
