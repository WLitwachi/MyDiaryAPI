
##!/usr/bin/env python!/usr/bin
# -*- coding: utf-8 -*-

"""Flask configuration for different environments."""

from __future__ import print_function

__all__ = '''
    Config
    ProductionConfig
    StagingConfig
    ExperimentalConfig
    TestingConfig
    DevelopmentConfig
    '''.split()

import flask.ext.config

Config = flask.ext.config.createConfig(__name__,
    updateEnvDefaults = dict(
        SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://dev:dev@localhost:3306/my_db'
    ))

# Configuration for different environments
class ProductionConfig(Config):
    """Configuration for production."""
    ENV_ID = 'prod'
    DEBUG = False

class StagingConfig(Config):
    """Configuration for staging
    """
    ENV_ID = 'stage'
    DEVELOPMENT = True
    DEBUG = True

class ExperimentalConfig(Config):
    """Configuration for experimental staging."""
    ENV_ID = 'try'
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    """Configuration for testing."""
    ENV_ID = 'qa'
    TESTING = True

class DevelopmentConfig(Config):
    """Configuration for development."""
    ENV_ID = 'dev'
    DEVELOPMENT = True
    DEBUG = True

# Aliases for different environment configurations
ProdConfig = ProductionConfig
StageConfig = StagingConfig
TryConfig = ExperimentalConfig
QaConfig = TestingConfig
TestConfig = TestingConfig
DevConfig = DevelopmentConfig

# Initialize requested config
Config.select()


# Print current configuration when run from command line
if __name__ == '__main__':
    print(Config)