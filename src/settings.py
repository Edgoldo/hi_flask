
class Config(object):
    """Base config."""
    DEBUG = True
    SECRET_KEY = 'efa2af4f82837e1a08b33650fe4ddde2b3fc101d9bf84a7c29f3355eb6507c96'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@db/hi_flask'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin123@localhost:5432/hi_flask'
    HOST_NAME = '0.0.0.0'
    PORT = '8080'
