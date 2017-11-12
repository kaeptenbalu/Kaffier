import os

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
    db_path = os.path.join(os.path.dirname(__file__), 'DevData.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(db_path)


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False
    SECRET_KEY = 'prod_key_change_this'
    db_path = os.path.join(os.path.dirname(__file__), 'Data.db')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(db_path)
    SQLALCHEMY_TRACK_MODIFICATION = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
