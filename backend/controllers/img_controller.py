from flask import Blueprint, request, jsonify
from bson.json_util import dumps
from utils.validation import validate_json
from schemas.img_schema import img_schema

img_blueprint = Blueprint("img_blueprint", __name__)

from database import (
    create_img as c,
    update_img as u,
    delete_img as d,
    get_img as g
)

@img_blueprint.route("/", methods=["POST"])
def create_img():
    img = request.json
    is_valid, error = validate_json(img, img_schema)
    if not is_valid:
        return jsonify({"message": error}), 400
    c(img)
    return jsonify({"message": "Image inserted succesfully"}), 201

@img_blueprint.route("/<img_id>", methods=["GET"])
def get_img(img_id):
    img = g(img_id)
    if img:
        return dumps(img)
    else:
        return jsonify({"message": "Img not found"}), 404
