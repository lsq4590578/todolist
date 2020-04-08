import os

here = os.path.dirname(__file__)

SECRET_KEY = 'flask-vue-todo-app'
WTF_CSRF_ENABLED = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

HOST_NAME = "192.168.1.24"
POST = 3306
USERNAME = "root"
PASSWORD = "123456"
DB = "hiqatools"

db_uri = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}".format(username=USERNAME, password=PASSWORD,
                                                                           host=HOST_NAME, port=POST, db=DB)
SQLALCHEMY_DATABASE_URI = db_uri
# SQLALCHEMY_TRACK_MODIFICATIONS = False

if 'DATABASE_URL' in os.environ:
    SQLALCHEMY_DATABASE_URI =db_uri
else:
    SQLALCHEMY_DATABASE_URI = db_uri
