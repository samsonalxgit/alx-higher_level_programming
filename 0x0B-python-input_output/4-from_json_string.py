#!/usr/bin/python3
"""An object represented by a JSON string"""
import json


def from_json_string(my_str):
    """An object represented by a JSON string"""
    return json.loads(my_str)
