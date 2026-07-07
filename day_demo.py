import json
import os


def demo():
    sourcefile = open("profile.txt", "r")
    json.load(sourcefile)
