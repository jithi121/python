import json
import os


def demo():
    file_path = './profile.txt'

    sourcefile = open("profile.txt", "w")

    print("hello")

    print(type(sourcefile))
    # temp = json.load(sourcefile)
    print(sourcefile)

    # print("temp", temp)
    # print(type(temp))

    temp_list = [1,.2,3,4]
    sourcefile.write(temp_list)
    print('sourcefule', sourcefile)
    print(type(sourcefile))




demo()