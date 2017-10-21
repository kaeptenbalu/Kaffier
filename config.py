class Config(object):
    """
    Common configurations
    """


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True
    SECRET_KEY = 'dev_key'
    SQLALCHEMY_TRACK_MODIFICATION = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///DevData.db'


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False
    SECRET_KEY = 'prod_key_change_this'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///Data.db'
    SQLALCHEMY_TRACK_MODIFICATION = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
