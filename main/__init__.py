from flask import Flask, session, abort, g
from flask_sqlalchemy import SQLAlchemy
import os
# from flask_mysqldb import MySQL
#import psycopg2
# from flask_mail import Mail, Message
app = Flask(__name__)
secret_key = os.urandom(16)
app.secret_key = secret_key

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'santi987'
# app.config['MYSQL_DB'] = 'inmobiliaria'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = False
#app.config['SQLALCHEMY_DATABASE_URI'] = (os.environ['DATABASE_URL'])
app.config['SQLALCHEMY_DATABASE_URI'] =  'mysql+pymysql://manuu307:8UQHX2AxU7b@manuu307.mysql.pythonanywhere-services.com/pallaresyasociados' 
#'sqlite:///database/database_two.db'
app.config['WTF_CSRF_ENABLED'] = False

db = SQLAlchemy(app)
# mail = Mail(app)

from main import routes

