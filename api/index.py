# app.py or main.py
from flask import Flask
from api.index import hello_world  # Your existing endpoint
from api.test import test_bp        # The new endpoint

app = Flask(__name__)

# Register the test blueprint
app.register_blueprint(test_bp)

@app.route("/api/python", methods=["GET", "POST"])
def hello_world():
   return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
