from flask import Flask
from .test import test_bp   
from flask_cors import CORS # type: ignore


app = Flask(__name__)
CORS(app)
app.register_blueprint(test_bp)

@app.route("/api/python", methods=["GET", "POST"])
def hello_world():
   return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
