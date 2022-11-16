import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@" \
                              f"{os.getenv('POSTGRES_HOST')}:5432/{os.getenv('POSTGRES_DB')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False