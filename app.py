from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
# This initiates the flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'
db = SQLAlchemy(app)

# Database Class 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    email = db.Column(db.String)

@app.route('/')
def index():
    return "Hello, World!"



if (__name__ == "__main__"): 
   app.run(debug=True)


