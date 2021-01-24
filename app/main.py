from flask import Flask
from flask import jsonify
import datetime
import socket

app = Flask(__name__)


@app.route("/")
def helloIndex():
    return 'Hello World !!'



@app.route("/quote")
def quote():
    return 'Agile and DevOps are for harnessing integration, interaction, and innovation. ―  Pearl Zhu'
