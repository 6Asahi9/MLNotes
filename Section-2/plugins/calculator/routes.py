from flask import Blueprint, request, jsonify

calc_bp = Blueprint("calculator", __name__, url_prefix="/calc")

@calc_bp.route("/add", methods=["GET"])
def add():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    return jsonify(result=a + b)

@calc_bp.route("/subtract", methods=["GET"])
def subtract():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    return jsonify(result=a - b)
