from pymongo import MongoClient
from bson import ObjectId
import random
from utils.midi import Midi
import os

client = MongoClient("mongodb://localhost:27017/")
db = client.nasa
img_collection = db.img
data_collection = db.data
sound_collection = db.sound
music_collection = db.music

# Funciones para img
def create_img(img_data):
    return img_collection.insert_one(img_data).inserted_id

def get_img(img_id):
    return img_collection.find_one({"_id": ObjectId(img_id)})

def update_img(img_id, updates):
    img_collection.update_one({"_id": ObjectId(img_id)}, {"$set": updates})

def delete_img(img_id):
    img_collection.delete_one({"_id": ObjectId(img_id)})

def get_music_from_img(img_id):
    img = get_img(img_id)
    return music_collection.find_one({"_id": img["music_id"]})

# Funciones para data
def create_data(data_info):
    return data_collection.insert_one(data_info).inserted_id

def get_data(data_id):
    return data_collection.find_one({"_id": ObjectId(data_id)})

def update_data(data_id, updates):
    data_collection.update_one({"_id": ObjectId(data_id)}, {"$set": updates})

def delete_data(data_id):
    data_collection.delete_one({"_id": ObjectId(data_id)})

def get_sound_from_data(data_id):
    data = get_data(data_id)
    return sound_collection.find_one({"_id": data["sound_id"]})

# Funciones para sounds
def create_sound(sound_data):
    return sound_collection.insert_one(sound_data).inserted_id

def get_sound(sound_id):
    return sound_collection.find_one({"_id": ObjectId(sound_id)})

def update_sound(sound_id, updates):
    sound_collection.update_one({"_id": ObjectId(sound_id)}, {"$set": updates})

def delete_sound(sound_id):
    sound_collection.delete_one({"_id": ObjectId(sound_id)})

# Funciones para music
def create_music(music_data):
    return music_collection.insert_one(music_data).inserted_id

def get_music(music_id):
    return music_collection.find_one({"_id": ObjectId(music_id)})

def update_music(music_id, updates):
    music_collection.update_one({"_id": ObjectId(music_id)}, {"$set": updates})

def delete_music(music_id):
    music_collection.delete_one({"_id": ObjectId(music_id)})

def get_sounds_from_music(music_id):
    music = get_music(music_id)
    return list(sound_collection.find({"_id": {"$in": music["sound_ids"]}}))

# Funciones compuestas
def get_all_data_from_img(img_id):
    img_data = []
    data_entries = list(data_collection.find({"img_id": ObjectId(img_id)}))
    for data_entry in data_entries:
        sound = get_sound_from_data(data_entry["_id"])
        img_data.append({"data": data_entry, "sound": sound})
    return img_data

def get_all_info_from_img(img_id):
    music = get_music_from_img(img_id)
    sounds = get_sounds_from_music(music["_id"])
    data_info = get_all_data_from_img(img_id)
    return {"img": get_img(img_id), "music": music, "sounds": sounds, "data_info": data_info}

def get_random_sound():
    sounds = list(sound_collection.find({}))
    return random.choice(sounds) if sounds else None

def get_random_image_with_music_id(music_id):
    main_image = img_collection.find_one({"music_id": ObjectId(music_id)})
    
    other_images = list(img_collection.find({"_id": {"$ne": main_image["_id"]}}).limit(3))
    
    all_images = [main_image] + other_images
    random.shuffle(all_images)
    
    return all_images

def compare_answers(music_id, image_id):
    image_1 = img_collection.find_one({"music_id": ObjectId(music_id)})
    image_2 = img_collection.find_one({"_id": ObjectId(image_id)})
    if image_1["_id"] == image_2["_id"]:
        return True
    else:
        return False #cambiar a lo que alberto quiere
