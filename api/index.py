from flask import Flask
from flask import Blueprint, request, jsonify
app = Flask(__name__)

@app.route("/api/python", methods=["GET","POST"])
def hello_world():
    data = request.get_json()
    
    # Assicurati che ci siano dati
    if data:
        # Aggiungi "ricevuto" all'input
        response = f"{data.get('input', '')} ricevuto"
        return jsonify({"response": response}), 200
    else:
        return jsonify({"error": "Nessun dato ricevuto"}), 400
