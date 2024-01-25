from flask import Flask, jsonify
from flask_cors import CORS

from start_config import *

app = Flask(__name__)
CORS(app)

API_HOST = api_cfg["API_HOST"]
API_PORT = api_cfg["API_PORT"]

# GET
@app.route("/", methods=["GET"])
def home():
    '''
    'Página inicial
    '''
    return "Proyecto FLASK"

if __name__ == "__main__":
    app.run(host=API_HOST, debug=True, port=API_PORT)