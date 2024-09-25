# app.py o main.py
from flask import Flask
from test import test_bp  # Importa il blueprint per il test

app = Flask(__name__)

# Registrazione del blueprint per il test
app.register_blueprint(test_bp)

@app.route("/api/python", methods=["GET", "POST"])
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
