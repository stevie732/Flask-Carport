import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))
class Config():

    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You"re Dead Meat!'
    SQLALCHEMY_DATABASE_URI = "postgresql://innhyizd:gJLYDzEZo8WQR00DDc8BTfkz42Co5305@isilo.db.elephantsql.com/innhyizd"