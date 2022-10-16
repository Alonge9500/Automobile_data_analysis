from flask import Flask
import os

app = Flask(__name__, template_folder="Template")
app.config['SECRET_KEY'] = '7ywy63789299hf5'




from webpage import route