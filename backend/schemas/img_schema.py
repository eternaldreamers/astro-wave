img_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "image_link": {"type": "string"},
        "music_id": {"type": "string", "format": "uuid"}
    },
    "required": ["name", "image_link"]
}