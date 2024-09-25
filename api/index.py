# api/index.py
from flask import Flask, request, jsonify
from .test import test_blueprint 

app = Flask(__name__)

@app.route("/api/python", methods=["GET", "POST"])
def hello_world():
    return "<p>Ciao, World!</p>"

# Registra il blueprint
app.register_blueprint(test_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
