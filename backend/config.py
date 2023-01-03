from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
caminho = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(caminho, "Hemos.db")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)