import json
import os
from ..utils.string_utils import to_snake_case

def load_json(path):
    with open(path) as f:
        return json.load(f)

def load_env(prefix=""):
    prefix = to_snake_case(prefix)
    return {f"{k[len(prefix):]}".lower(): v for k, v in os.environ.items() if k.startswith(prefix.upper()) or k.startswith(prefix.lower())}
