# api/test.py
from flask import Blueprint, request, jsonify

# Creazione del blueprint per il nuovo endpoint
test_bp = Blueprint('test', __name__)

@test_bp.route("/api/test", methods=["GET", "POST"])
def test():
    # Ottieni i dati JSON dalla richiesta
    data = request.get_json()
    
    # Assicurati che ci siano dati
    if data:
        # Aggiungi "ricevuto" all'input
        response = f"{data.get('input', '')} ricevuto"
        return jsonify({"response": response}), 200
    else:
        return jsonify({"error": "Nessun dato ricevuto"}), 400
