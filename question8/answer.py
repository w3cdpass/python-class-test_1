import sys # build-in function use for what i don't know  
victory = 0
loses = 0
ties = 0
print("""    Stone Paper Scissor game 🎮 
      🪨    ⬜     ✂️""")


# exit the game 
while True:
    # input method tag here
    player_input = input("Enter a pick [Stone, Paper, Scissor]: ").lower()

    # exiting the game loop
    if player_input == "x":
        print("Exiting the game")
        sys.exit()
    else:
        # our computer picks that are random 
        computer_input = {"stone", "paper", "scissor"}
        pick_one_key_value1 = computer_input.pop()# << this pop up methon will give us a one value (that is remove by .pop())

        # decalring the picks 
        '''What Player: pick and Computer: pick'''
        print(f"You enter: {player_input}.")
        print(f"Computer pick: {pick_one_key_value1}")

        if player_input == pick_one_key_value1:
            print("it's tie")
            print(f"Ties: {ties + 1}")
            # player_input = input("Enter a pick [Stone, Paper, Scissor]: ").lower()
        else:
            if player_input == "stone" and pick_one_key_value1 == "scissor":
                print(" 🪨   VS  ✂️ \nYou win.")
                print(f"Victory: {victory + 1}")
                # player_input = input("Enter a pick [Stone, Paper, Scissor]: ").lower()
            elif player_input == "paper" and pick_one_key_value1 == "stone":
                print(" 📰   VS  🪨 \nYou win")
                print(f"Victory: {victory + 1}")
                # player_input = input("Enter a pick [Stone, Paper, Scissor]: ").lower()
            elif player_input == "scissor" and pick_one_key_value1 == "paper":
                print(" ✂️   VS   📰 \nYou win ")
                print(f"Victory: {victory + 1}")
                # player_input = input("Enter a pick [Stone, Paper, Scissor]: ").lower()
            else:
                if pick_one_key_value1 == "stone" and player_input == "scissor":
                    print(" 🪨   VS  ✂️ \nYou lose.")
                    print(f"Loses: {loses + 1}")
                    # player_input = input("Enter a pick [Stone, Paper, Scissor]: ").lower()
                elif pick_one_key_value1 == "paper" and player_input == "stone":
                    print(" 📰   VS  🪨 \nYou lose")
                    print(f"Loses: {loses + 1}")
                    player_input = input("Enter a pick [Stone, Paper, Scissor]: ").lower()
                elif pick_one_key_value1 == "scissor" and player_input == "paper":
                    print(" ✂️  VS   📰 \nYou lose ")
                    print(f"Loses: {loses + 1}")
                    # player_input = input("Enter a pick [Stone, Paper, Scissor]: ").lower()