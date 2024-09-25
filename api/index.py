from flask import Flask
from flask_cors import CORS

from test import test_bp     

app = Flask(__name__)
CORS(app)
# Registrazione dei blueprints

app.register_blueprint(test_bp)

if __name__ == "__main__":
    app.run(debug=True)
