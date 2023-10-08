from flask import Blueprint, request, jsonify
from bson.json_util import dumps
from utils.validation import validate_json
from schemas.data_schema import data_schema

data_blueprint = Blueprint("data_blueprint", __name__)

from database import (
    create_data as c,
    update_data as u,
    delete_data as d,
    get_data as g
)

@data_blueprint.route("/", methods=["POST"])
def create_data():
    data = request.json
    is_valid, error = validate_json(data, data_schema)
    if not is_valid:
        return jsonify({"message": error}), 400
    c(data)
    return jsonify({"message": "Data inserted succesfully"}), 201

@data_blueprint.route("/<data_id>", methods=["GET"])
def get_data(data_id):
    data = g(data_id)
    if data:
        return dumps(data)
    else:
        return jsonify({"message": "data not found"}), 404

@data_blueprint.route("/<data_id>", methods=["PUT"])
def update_data(data_id):
    updates = request.json
    u(updates)
    return jsonify({"message": "data updated successfully"}), 200

@data_blueprint.route("/<data_id>", methods=["DELETE"])
def delete_data(data_id):
    d(data_id)
    return jsonify({"message": "data deleted successfully"}), 200