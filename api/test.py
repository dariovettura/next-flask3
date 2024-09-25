# api/test.py
from flask import Blueprint, request, jsonify

# Create a new blueprint for the test endpoint
test_bp = Blueprint('test', __name__)

@test_bp.route("/api/test", methods=["GET", "POST"])
def test_endpoint():
    data = request.get_json()
    
    # Check if data is received
    if data:
        # Process input or simply return a message
        response = f"Test endpoint received: {data.get('input', '')}"
        return jsonify({"response": response}), 200
    else:
        return jsonify({"error": "No data received"}), 400
