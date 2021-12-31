from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# import secrets
# secret_key = secrets.token_hex(16)
app.config["SECRET_KEY"] = 'd8eed0b0a295ca457ea8def492983b00'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from mysite import routes