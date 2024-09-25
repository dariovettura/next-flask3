# api/test.py
from flask import Blueprint, request, jsonify

# Creazione del blueprint per il nuovo endpoint
test_bp = Blueprint('test', __name__)

@test_bp.route("/api/test", methods=["GET", "POST"])
def test_endpoint():
    # Per testare l'endpoint senza input
    return jsonify({"message": "ok"}), 200  # Risposta di successo
