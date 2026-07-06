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
import pyinputplus


def exit_menu():
    print('shutting down, till next time')
    exit()    

def insert_details(profile_list):

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
    
    profile_list.write(names)

    temp_file = json.dumps(profile_list)
    # print(type(temp_file))
    with open("profile.txt","a") as f:
        f.write(temp_file)


def Read_file(profile_list):
    os.system('cls')
    print("Profile list")
    with open("profile.txt") as f:
        print(f.read())



def land_page():

    file_path = './profile.txt'
    print('hi')
    if os.path.exists(file_path):
        print('exist, no need for fresh array')
        profile_list = open("profile.txt", "w")
        print(type(profile_list))


    else:
        print('new list created')
        profile_list = open("profile.txt", "x")
        # global profile_list
        # profile_list = [];



    while True:
        
        try:
        #Main landing page with options
            
            
            Landing_page = int(input("""Welcome to the Profile Creator! 
                        
                        Please select an option:
                        
                        1 : Create a new user
                        2 : show all users in profile
                        3 : Exit \n\n"""))
        except ValueError:
            print("Almost there, try a number from the menu!")
            
        else:
            if type(Landing_page) is int:


                match Landing_page:
                   
                    case 1:
                       insert_details(profile_list)
                    case 2:
                        Read_file(profile_list)
                    case 3:
                    #Exit command from application. Shutsdown
                      exit_menu()    
                    case _:
                        os.system('cls')
                        print('try again, incorrect option detected. returning back in 3 secs')
                        
                        i = 3
                        while i>0:

                            print('returning back in ' + str(i) + ' seconds')
                            i = i-1 
                            # time.sleep(3)
                            os.system('cls')
            else:
                print("try numbers, perhaps!")


land_page()












