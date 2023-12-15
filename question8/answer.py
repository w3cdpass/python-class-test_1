# input_player = input("enter a input: ")
# computer_Player = ""
# typo = set(list({"rock","paper","scissor"}))
# print(randon)
# if input_player == "rock" or computer_Player == typo :
#     print("u win")
#     print(f"{typo}")
# else:
#     print("lose")

# list_name = 'Mi Apple Samsung Mi Apple Realme Oppo Samsung Oppo Vivo'.split()
# print(list_name)
# new_set = {'Mi', 'Apple', 'Samsung', 'Mi', 'Apple', 'Realme', 'Oppo', 'Samsung', 'Oppo', 'Vivo'}
# print(type(new_set))
# sndnew_list = list(new_set)
# print(sndnew_list)
player_input = input("enter here: ")
game_sps = {
    "computer_input": # << declaring a dictonary with some argument like{key:vlaue pairs}
        {"stone", "paper", "scissor"} # << there are value pairs
        }
computer_input = game_sps["computer_input"]# << this will tigger the argument what is in key of their values 
# list_of_computer = list(set(computer_input))
# print(list_of_computer) 
pick_one_key_value = computer_input.pop()# << this pop up methon will give us a one value
print(f"Computer pick: {pick_one_key_value}")
# sps_list = list(set(game_sps))
# print(sps_list)
# player_input = input("Enter s p s : ")
# # computer_input = {"scissor","paper","stone"}
# # list_of_com = list(set(computer_input))
# # print(list_of_com)
# computer_input = [sps_list]
# if player_input == "rock" or computer_input == sps_list:
#     print(f"{computer_input} u win  ")
# else:
#     print(f"{sps_list} random")
if player_input == pick_one_key_value:
    print("it's tie")
else:
    if player_input == "stone" and pick_one_key_value == "scissor":
        print(f"You pick: {player_input} and computer pick: {pick_one_key_value}\nYou win.")
    elif player_input == "paper" and pick_one_key_value == "rock":
        print(f"You pick: {player_input} and computer pick: {pick_one_key_value}\nYou win")
    elif player_input == "scissor" and pick_one_key_value == "paper":
        print(f"You pick: {player_input} and computer pick: {pick_one_key_value}\nYou win ")
    else:
        print(f"Your pick: {player_input} and computer pick: {pick_one_key_value}\nYou lose.")
