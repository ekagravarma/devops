from gunicorn_app import app
from flask import render_template

@app.route("/")
def home():
    #return render_template('index.html')
    return "Hi! My name is Ekagra .\n This is a project on building Multi-stage Dockerfile"
