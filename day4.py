# Since we're treating this like a real software project, I'd like you to use commits that fall into categories like:

# feat: → New feature
# fix: → Bug fix
# refactor: → Code restructuring (no new functionality)
# docs: → Documentation changes
# style: → Formatting/readability only
# test: → Tests added or updated
# chore: → Maintenance tasks

# persistence first (load/save properly, single source of truth)
# validation next (stop bad mem_data entering the system)
# cleanup last (refactor structure once behaviour is stable)

import os
import json
import datetime


def exit_menu():
                                                                                    # takes care of exiting program
    print('shutting down, till next time')
    exit()    

def insert_details(mem_data):
                                                                                    # takes care of insert operations  
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
    time_stamp = datetime.datetime.now()
    
    names = {'name':name, 'age':age, 'fav_tool':fav_tool, 'age_group':age_group, 'time_stamp': time_stamp.strftime("%c") }
    mem_data.append(names)    
    print(mem_data)
    print('entry added at ', time_stamp.strftime("%c"))

    with open("profile.txt","w") as f:
        json.dump(mem_data,f)

                                                                                    # learned about TextIOWrapper 
                                                                                    # how to convert to JSON
                                                                                    # how to open, read, write and append to file 
                                                                                    # function calls 
                                                                                    # importing JSON, converting to JSON
                                                                                    # converting list to txt file and back  


def read_file(mem_data):                                                                
    os.system('cls')
    print(mem_data)
    with open("profile.txt") as f:
        print(f.read())
                                                                                    # take care of print database

def land_page():
                                                                                    # landing page 
    mem_data = []

    file_path = './profile.txt'

    if os.path.exists(file_path):

        # print('exist, no need for fresh array')
        data_base = open("profile.txt", "r")

        # print(type(data_base))
        # print(data_base)
        mem_data = json.load(data_base)
        # print(mem_data)

        if not mem_data:
            initial_list = [];
            mem_data = initial_list;
            # data_base.write(initial_list)
        
            # mem_data = json.load(data_base)
            print('file has been loaded')

            

    else:
        print('new list created')
        data_base = open("profile.txt", "a")
        # mem_data = json.load(data_base)
        mem_data

    while True:
        
        try:            
                                                                                        # user input screen
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
                       insert_details(mem_data)
                    case 2:
                        read_file(mem_data)
                    case 3:
                      exit_menu()    
                    case _:
                        os.system('cls')
                        print('Incorrect entry, please try again')

land_page()












