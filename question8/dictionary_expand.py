# dic_tio = {1:"I", 2:"am", 3:"good", 4:"men"}

# print(dic_tio)
# dic_tio = {"name":"geek", 1:[1,2,3,4]}
# print(dic_tio)

# dic_tio2 = list(dic_tio) # while converting into list they can't be show key value pairs
# print(dic_tio2)

# dict_ion = ([(1,'Rohit'),(2, "kumar")])
# print(type(dict_ion))
# print(dict_ion)

# nested_dict = {
    
#     'first name': "rohit",
#     'last name': "kumar",
#     'age': 30,
#     'gender': 'male',
#     'address': {
#         'street' : "near airport",
#         'city' : 'chandighar',
#         'pin_code': 150400,
#     },
#     'contacts': {
#         'email': 'rhotku@gmail.com',
#         'phone_no': 123456789
#     }

# }


# first_name,last_name = nested_dict['first name'], nested_dict['last name']
# print(f"Name: {first_name} {last_name}")

# # address
# city_info = nested_dict['address']['city']
# print(city_info)

# # contacts

# cont_info = nested_dict['contacts']['email']
# print(cont_info)

# age_info = nested_dict["age"]
# print(age_info)

# # modifying dictionary 

# modified = nested_dict['age'] = 25
# print(modified)


# # into key values
# nested_dict['address']['street'] = 'shop:34' 
# print(nested_dict)


# print(nested_dict)

# nested_dict.clear()
# nested_dict.copy()
# get_method = nested_dict.get('first name', 'last name') # to use get method (value = dictionary.get(key,default))
# print(get_method)

# dictionary.items()
# item_list = list(nested_dict.items())
# convert_list = list(item_list)
# print(convert_list)

# keys_view = nested_dict.popitem() # pop in dict is the method that remove and return a specified key value from dictionary

# print(f"Removed key-value pair {keys_view}")
# print("modify dictionary", nested_dict)

# serqurity game 

house_of_paper = {
    "theif_type" :
        {"robbery 🥸 ", "Bicycle_thef 🏍️" ,"preciouslifting 🔷💠"}
}

# print(house_of_paper)
# random crime
random_thef = house_of_paper['theif_type']

# one crime at time 
one_crime_atime = random_thef.pop()
print(f"Hey! I'm {one_crime_atime}")

# set conditons to capture that person
# "robbery", "Bicycle_thef" ,"preciouslifting"
if one_crime_atime == "preciouslifting 🔷💠":
    print(f"Alert preciouslifter! 🛑 Stop it's police stop {one_crime_atime}👮.")
elif one_crime_atime == "Bicycle_thef 🏍️":
    print(f"Alert Bicycle thef! 🛑 handsup it's police stop {one_crime_atime}👮")
else:
    print(f"Alert Robber !. It's police 👮  handsup robber.")
    
