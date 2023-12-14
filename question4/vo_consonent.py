# user_name = input("Enter ur username")
# pass_wd = input("Enter ur passwd")


# # and 
# # logical oprator 

# if user_name == "Ram" or pass_wd == "password":
#     print(f"Hi! {user_name}.Login successful")
# else:
#     print(f"{user_name} and {pass_wd} is incorrect")



# or one should be one argument should be true
# and both of them argument should be be true
vovals = input("enter a vovals: ").lower()
# cosonent = input("enter a consonent")\
if len(vovals) == 1:
    if vovals.isalnum():
        if vovals in "aeiouAEIOU":
            print("vovals")
        elif vovals not in  "aeiouAEIOU":
            print("consonent")
        else:
            print("invalid")
    else:
        print("Enter a valid alphabet")
print("Enter a single alphabet")
# upper should be uppercase and lowercase / 

# if vovals not in "aeiou" :
#         print("invalid")
#     else:
#         print("Correct! Vovals Here.")

# calculate  the income tax of an employee