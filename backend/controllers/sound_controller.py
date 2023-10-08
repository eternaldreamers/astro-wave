from flask import Blueprint, request, jsonify
from bson.json_util import dumps
from utils.validation import validate_json
from schemas.sound_schema import sounds_schema

sound_blueprint = Blueprint("sound_blueprint", __name__)

from database import (
    create_sound as c,
    update_sound as u,
    delete_sound as d,
    get_sound as g
)

@sound_blueprint.route("/", methods=["POST"])
def create_sound():
    sound = request.json
    is_valid, error = validate_json(sound, sounds_schema)
    if not is_valid:
        return jsonify({"message": error}), 400
    c(sound)
    return jsonify({"message": "Sound inserted succesfully"}), 201

@sound_blueprint.route("/<sound_id>", methods=["GET"])
def get_sound(sound_id):
    sound = g(sound_id)
    if sound:
        return dumps(sound)
    else:
        return jsonify({"message": "sound not found"}), 404

@sound_blueprint.route("/<sound_id>", methods=["PUT"])
def update_sound(sound_id):
    updates = request.json
    u(sound_id, updates)
    return jsonify({"message": "sound updated successfully"}), 200

@sound_blueprint.route("/<sound_id>", methods=["DELETE"])
def delete_sound(sound_id):
    d(sound_id)
    return jsonify({"message": "sound deleted successfully"}), 200