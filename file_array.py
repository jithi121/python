import json

my_list = ['a' 'c', 's', 's']

with open('fruits.json', 'a') as file:
    json.dump(my_list, file, indent=4)   
    


