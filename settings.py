import os

SECRET_KEY = os.getenv('SECRET_KEY')
DB_USERNAME='counter_app'
DB_PASSWORD='mypassword'
DB_HOST='localhost'
DATABASE_NAME='counter'
DB_URI = 'mysql+pymysql://%s:%s@%s:3306/%s' % (DB_USERNAME, DB_PASSWORD, DB_HOST, DATABASE_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
