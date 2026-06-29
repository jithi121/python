import os
import json
import time

profile_list = [];

def exit_menu():
    print('shutting down, till next time')
    exit()    

def insert_details():
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
    
    profile_list.append(names)

    temp_file = json.dumps(profile_list)
    # print(type(temp_file))
    with open("profile.txt","a") as f:
        f.write(temp_file)


def Read_file():
    print("Profile list")
    with open("profile.txt") as f:
        print(f.read())



def land_page():
    while True:
        
        try:
        #Main landing page with options
            
            Landing_page = int(input("""Welcome to the Profile Creator! 
                        
                        Please select an option:
                        
                        1 : Create a new profile
                        2 : show all users in a profile
                        3 : Exit \n\n"""))
        except ValueError:
            print("Almost there, try a number from the menu!")
            
        else:
            if type(Landing_page) is int:


                match Landing_page:
                   
                    case 1:
                       insert_details()
                    case 2:
                        Read_file()
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












