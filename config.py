# adjust the Config class below, then rename this file to config.py


class DefaultConfig(object):
    # a decent way to generate a secret key is by running: python -c "import os; print(repr(os.urandom(24)))"
    # then pasting the output here.
    SECRET_KEY = "secret_key_change_me"

    DEBUG = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "postgres://keyserver:keyserver@db/keyserver"

class ProductionConfig(DefaultConfig):
    SQLALCHEMY_DATABASE_URI = "postgres://keyserver:keyserver@db/keyserver"
    pass

class DevelopmentConfig(ProductionConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
