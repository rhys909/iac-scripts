from app import app
import os

@app.route("/")
def index():

    return "Testing Flask and Nginx webserver on RPi :)"
