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

# game_sps = {
#     "computer_input": # << declaring a dictonary with some argument like{key:vlaue pairs}
#         {"stone", "paper", "scissor"} # << there are value pairs
#         }
# computer_input = game_sps["computer_input"]# << this will tigger the argument what is in key of their values 
# list_of_computer = list(set(computer_input))
# print(list_of_computer) 
# sps_list = list(set(game_sps))
# print(sps_list)
# player_input = input("Enter s p s : ")
# # computer_input = {"scissor","paper","stone"}
# # list_of_com = list(set(computer_input))
# # print(list_of_com)
# computer_input = [sps_list]
# if player_input == "rock" or computer_input == pick_one_key_value:
#     print(f"{computer_input} u win  ")
# else:
#     print(f"{pick_one_key_value} random")
victory = 0
loses = 0
ties = 0
print("""    Stone Paper Scissor game 🎮 
      🪨    ⬜     ✂️""")
player_input = input("Enter a pick [Stone, Paper, Scissor]: ").lower()

computer_input = {"stone", "paper", "scissor"}
pick_one_key_value = computer_input.pop()# << this pop up methon will give us a one value
print(f"You pick: {player_input}.")
print(f"Computer pick: {pick_one_key_value}")

if player_input == pick_one_key_value:
    print("it's tie")
    print(f"Ties: {ties + 1}")
else:
    if player_input == "stone" and pick_one_key_value == "scissor":
        print(" 🪨   VS  ✂️ \nYou win.")
        print(f"Victory: {victory + 1}")
    elif player_input == "paper" and pick_one_key_value == "stone":
        print(" 📰   VS  🪨 \nYou win")
        print(f"Victory: {victory + 1}")
    elif player_input == "scissor" and pick_one_key_value == "paper":
        print(" ✂️   VS   📰 \nYou win ")
        print(f"Victory: {victory + 1}")
    else:
        if pick_one_key_value == "stone" and player_input == "scissor":
            print(" 🪨   VS  ✂️ \nYou lose.")
            print(f"Loses: {loses + 1}")
        elif pick_one_key_value == "paper" and player_input == "stone":
            print(" 📰   VS  🪨 \nYou lose")
            print(f"Loses: {loses + 1}")
        elif pick_one_key_value == "scissor" and player_input == "paper":
            print(" ✂️  VS   📰 \nYou lose ")
            print(f"Loses: {loses + 1}")
