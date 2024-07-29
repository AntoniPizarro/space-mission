#import threading
from flask import Flask, jsonify, render_template
from flask_cors import CORS

from config import api_cfg
from service import *

DEV_MODE = True

app = Flask(__name__, template_folder='./web_site/templates/', static_folder="./web_site/static/")
CORS(app)

API_HOST = api_cfg["HOST"]
API_PORT = api_cfg["PORT"]

# GET
@app.route("/site", methods=["GET"])
def home():
    return api_cfg["title"]

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    # Tareas por hilos
    #thread_get_commits = threading.Thread(target=get_all_commits)
    #thread_get_commits.start()

    # Ejecutamos la aplicación de Flask
    app.run(host=API_HOST, debug=DEV_MODE, port=API_PORT)