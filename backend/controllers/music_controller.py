from flask import Blueprint, request, jsonify
from bson.json_util import dumps
from utils.validation import validate_json
from schemas.music_schema import music_schema

music_blueprint = Blueprint("music_blueprint", __name__)

from database import (
    create_music as c,
    update_music as u,
    delete_music as d,
    get_music as g
)


@music_blueprint.route("/", methods=["POST"])
def create_music():
    music = request.json
    is_valid, error = validate_json(music, music_schema)
    if not is_valid:
        return jsonify({"message": error}), 400
    c(music)
    return jsonify({"message": "Music inserted succesfully"}), 201

@music_blueprint.route("/<music_id>", methods=["GET"])
def get_music(music_id):
    music = g(music_id)
    if music:
        return dumps(music)
    else:
        return jsonify({"message": "music not found"}), 404

@music_blueprint.route("/<music_id>", methods=["PUT"])
def update_music(music_id):
    updates = request.json
    u(updates)
    return jsonify({"message": "music updated successfully"}), 200

@music_blueprint.route("/<music_id>", methods=["DELETE"])
def delete_music(music_id):
    d(music_id)
    return jsonify({"message": "music deleted successfully"}), 200