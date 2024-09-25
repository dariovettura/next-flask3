from flask import Flask

from test import test_bp     

app = Flask(__name__)

# Registrazione dei blueprints

app.register_blueprint(test_bp)

if __name__ == "__main__":
    app.run(debug=True)
