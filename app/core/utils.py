# app/core/utils.py

from typing import Any
import json


def to_json(data: Any) -> str:
    """Convert data to JSON string."""
    return json.dumps(data)
