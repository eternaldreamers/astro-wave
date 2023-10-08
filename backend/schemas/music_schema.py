music_schema = {
    "type": "object",
    "properties": {
        "sound_ids": {
            "type": "array",
            "items": {"type": "string", "format": "uuid"}
        }
    },
    "required": ["sound_ids"]
}
