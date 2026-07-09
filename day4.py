# Since we're treating this like a real software project, I'd like you to use commits that fall into categories like:

# feat: → New feature
# fix: → Bug fix
# refactor: → Code restructuring (no new functionality)
# docs: → Documentation changes
# style: → Formatting/readability only
# test: → Tests added or updated
# chore: → Maintenance tasks

# persistence first (load/save properly, single source of truth)
# validation next (stop bad data entering the system)
# cleanup last (refactor structure once behaviour is stable)

import os
import json
import time


def exit_menu():
    print('shutting down, till next time')
    exit()    

def insert_details(data):

    name = input('Please enter your name: ')
    os.system('cls')

    age = int(input('Please enter your age: '))
    os.system('cls')

    if age<18:
        age_group = 'minor'
    else:
        age_group = 'adult'

    fav_tool = input('Please enter your favorite tool: ')
    os.system('cls')

    names = {'name':name, 'age':age, 'fav_tool':fav_tool, 'age_group':age_group}
    data.append(names)    
    print(data)
    print('worked until here' )

    with open("profile.txt","w") as f:
        json.dump(data,f)

# learned about TextIOWrapper 
# how to convert to JSON
# how to open, read, write and append to file 
# function calls 
# importing JSON, converting to JSON
# converting list to txt file and back  


def read_file(data):
    os.system('cls')
    print(data)
    with open("profile.txt") as f:
        print(f.read())



def land_page():

    data = []

    file_path = './profile.txt'

    if os.path.exists(file_path):

        print('exist, no need for fresh array')
        local_file = open("profile.txt", "r")

        if not local_file:
            initial_list = [];
            local_file.write(initial_list)
        
            data = json.load(local_file)
            print('file has been loaded')
            

    else:
        print('new list created')
        local_file = open("profile.txt", "a")
        data = json.load(local_file)
        return data

    while True:
        
        try:            
            
            landing_page = int(input("""Welcome to the Profile Creator! 
                        
                        Please select an option:
                        
                        1 : Create a new user
                        2 : show all users in profile
                        3 : Exit \n\n"""))
        except ValueError:
            print("Please input correct options")
            
        else:
            if type(landing_page) is int:

                match landing_page:
                   
                    case 1:
                       insert_details(data)
                    case 2:
                        read_file(data)
                    case 3:
                      exit_menu()    
                    case _:
                        os.system('cls')
                        print('Incorrect entry, please try again')

land_page()












