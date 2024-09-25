from flask import Flask
from .test import test_bp   

app = Flask(__name__)



@app.route("/api/python", methods=["GET", "POST"])
def hello_world():
   return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
