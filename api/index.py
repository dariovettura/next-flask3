from flask import Flask
from flask import Blueprint, request, jsonify
from .test import test_blueprint 
app = Flask(__name__)

@app.route("/api/python", methods=["GET","POST"])
def hello_test():
    return "<p>Ciao, World!</p>"


app.register_blueprint(test_blueprint)
if __name__ == "__main__":
    app.run()