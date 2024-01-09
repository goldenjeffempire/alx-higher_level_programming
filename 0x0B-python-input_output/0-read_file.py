#!/usr/bin/python3
"""Defines a text file-reading function."""

def read_file(filename=""):
    with open(filename, "r",
encoding="utf8") as file:
    contents = file.read()
    print(contents)
