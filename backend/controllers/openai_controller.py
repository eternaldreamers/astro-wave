from flask import Blueprint, request, jsonify
import os
from services.openia import Openia
from bson import ObjectId
from database import data_collection

openai_blueprint = Blueprint("openai_blueprint", __name__)
gpt = Openia(os.getenv("GPT4_API_KEY"))

def get_differences(data1, data2):
    differences = {}
    for key in data1:
        if key not in ["_id", "img_id"] and data1[key] != data2[key]:
            differences[key] = (data1[key], data2[key])
    return differences

@openai_blueprint.route("/", methods=["POST"])
def chat():
    message = request.json["message"]
    response = gpt.teach(message)
    return jsonify({"response": response})

@openai_blueprint.route("/compare", methods=["POST"])
def compare():
    id_correct = request.json["id_correct"]
    id_incorrect = request.json["id_incorrect"]

    # Obtener los datos asociados con cada ID
    data_correct = data_collection.find_one({"img_id": id_correct})
    data_incorrect = data_collection.find_one({"img_id": id_incorrect})

    # Obtener las diferencias
    differences = get_differences(data_correct, data_incorrect)

    # Generar un mensaje para GPT
    message = "Explain the differences between these two sets of data:\n"
    for key, (val_correct, val_incorrect) in differences.items():
        message += f"{key}: {val_correct} (correct) vs {val_incorrect} (incorrect)\n"

    interpretation = gpt.interpret_differences(differences)
    detailed_message = f"""
Hey GPT! 🌌

Imagine you're a space guide explaining to a group of curious high school students. We're comparing two planets, and I've noticed some differences. Here's a brief summary: {interpretation}.

Given these differences, can you provide a fun and engaging explanation about why one of these planets might not be what the students initially thought? Remember, make it exciting and easy to understand!🚀
"""
    explanation = gpt.teach(detailed_message)

    return jsonify({"explanation": explanation})
