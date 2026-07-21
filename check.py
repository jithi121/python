import os
import json


file_path = './profile.txt'

if os.path.exists(file_path):

        # print('exist, no need for fresh array')
        data_base = open("profile.txt", "r")

        if not mem_data:
            initial_list = [];
            data_base.write(initial_list)
        
            print('file has been loaded')
