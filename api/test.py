from flask import Blueprint, request, jsonify

test_blueprint = Blueprint('test_blueprint', __name__)

@test_blueprint.route("/api/test", methods=['POST'])
def hello_test():
    # Ottieni i dati JSON dalla richiesta
    data = request.get_json()
    
    # Assicurati che ci siano dati
    if data:
        # Aggiungi "ricevuto" all'input
        response = f"{data.get('input', '')} ricevuto"
        return jsonify({"response": response}), 200
    else:
        return jsonify({"error": "Nessun dato ricevuto"}), 400
