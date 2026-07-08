import json
import os


def demo():
    file_path = './profile.txt'

    sourcefile = open("profile.txt", "r")
    print("hello")
    print(type(sourcefile))
    temp = json.load(sourcefile)
    print(sourcefile)

    print("temp", temp)
    print(type(temp))

demo()