bear_schema = {
    "type": "object",
    "title": "The bear schema",
    "required": [
        "bear_id",
        "bear_type",
        "bear_name",
        "bear_age"
    ],
    "properties": {
        "bear_id": {
            "$id": "#/properties/bear_id",
            "type": "number",
            "title": "Bear id"
        },
        "bear_type": {
            "$id": "#/properties/bear_type",
            "type": "string",
            "title": "Bear type"
        },
        "bear_name": {
            "$id": "#/properties/bear_name",
            "type": "string",
            "title": "Bear name",
            "default": ""
        },
        "bear_age": {
            "$id": "#/properties/bear_age",
            "type": "number",
            "title": "Bear age",
            "default": 0.0
        }
    },
    "additionalProperties": False
}
