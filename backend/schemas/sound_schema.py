sounds_schema = {
    "type": "object",
    "properties": {
        "data_property": {"type": "string", "enum": ["moons", "gravity", "temperature", "rings", "water", "craters", "radiation", "density", "size", "volcanoes", "auroras"]},
        "chord_progression": {
            "type": "array",
            "items": {"type": "string"}
        },
        "duration": {"type": "number"},
        "octave": {"type": "integer"},
        "track": {"type": "integer"}
    },
    "required": ["chord_progression", "duration", "octave", "track", "data_property"]
}
