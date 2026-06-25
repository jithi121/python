import os
import json
import time

profile_list = [];

while True:
    
    #Main landing page with options
    Landing_page = int(input("""Welcome to the Profile Creator! 
                  
                  Please select an option:
                  
                  1 : Create a new profile
                  2 : show all users in a profile
                  3 : Exit \n\n"""))


    match Landing_page:
        case 3:
            #Exit command from application. Shutsdown
            print('shutting down, till next time')
            exit()


        case 1:
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
            # print(name)

            profile_list.append(names)

            temp_file = json.dumps(profile_list)
            print(type(temp_file))
            with open("profile.txt","a") as f:
                f.write(temp_file)



        case 2:
            print("Profile list")
            # print(profile_list)
            with open("profile.txt") as f:
                print(f.read())

        case _:
            os.system('cls')
            print('try again, incorrect format detected.')
            
            
            for i in range(3):
                print(f'returning back in 3 seconds')
                time.sleep(3)
                os.system('cls')









