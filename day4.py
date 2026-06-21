

main_menu = int(input("""Welcome to the Profile Creator! 
                  
                  Please select an option:
                  
                  1 : Create a new profile
                  2 : show all users in a profile
                  3 : Exit"""))


match main_menu:
    case 3:
        print('shutting down, till next time')
        exit()
    case 1:
        print("1 up")
        name = input('Please enter your name: ')
        age = int(input('Please enter your age: '))
        if age<18:
            age_group = 'minor'
        else:
            age_group = 'adult'

        fav_tool = input('Please enter your favorite tool: ')

        name = {'name':name, 'age':age, 'fav_tool':fav_tool, 'age_group':age_group}
        print(name)

        profile_list = [];
        profile_list.append(name)
        print(profile_list)









