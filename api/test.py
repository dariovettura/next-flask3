
from flask import Blueprint, request, jsonify

test_bp = Blueprint('test', __name__)

@test_bp.route("/api/test", methods=["GET", "POST"])
def test_endpoint():
    return "ok"
