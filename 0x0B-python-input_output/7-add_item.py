#!/usr/bin/python3
"""add_item
"""
import sys
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

try:
    loadFile = load_from_json_file("add_item.json")
except FileNotFoundError:
    loadFile = []

argc = len(sys.argv)
for idx in range(1, argc):
    loadFile.append(sys.argv[idx])
save_to_json_file(loadFile, "add_item.json")
