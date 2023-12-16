# /project and be done 

# trip cost planner tie with hotels deals with for location and also u hav eyour fixed location office by plane cost it ="15000" by place [goa: ]

# per night is 1200 bucks and for travelin by cab and mean of transport 1000 per day/ after 5 days 2000 will be discounted 7 days will be 3000 discounted

# user name = name / how many days / location / how many days / what is ur budget / how many days u want to rent a car / totol should be calculated /if user has low budget u have to add money if not u can't travel/
# calculate your trip expenses 

'''^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'''

print("🚩 Welcome to Pulse Agency 🚩")
customer_name = input("Hi! What is your good name:  ")
            # ~~~~~ About our agency ~~~~~ 
print(f"""Hello! {customer_name} where you wanna travel.
    Our agency can help you.\nTo find out your best budget places in INDIA.""")

travel_places = int(input("""         ~~~ WE Can TRAVEL YOU ~~~
    CHANDIGHAR, LADAKH, ASSAM, BENGALURU
Press[1 for Chandighar, 2 for Ladakh, 3 for Assam, 4 for Bengaluru]: """))

'''^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'''

# First option 

if travel_places == 1:
    print("Great Place! You chose Chandighar.")
    chd_bdgt = int(input("Tell me your budget: "))
    if 5000 <= chd_bdgt and chd_bdgt < 10000:
        print(f"In this {chd_bdgt} of budget we can guide you!")
        mean_of_trnsprt = input("How do you want to go?\nAirplane ✈️  or bus 🚎: ")
        if mean_of_trnsprt == "Airplane":
            print("We can provide a ticket for you:✈️")
        else:
            print("Ok! We can book a bus for you:🚎")
        how_many_days = int(input("How many days you wanna stay in hotel 🏨:"))
        if how_many_days < 5:
            print("OK then We booked a hotel 🏨 for You")
        elif how_many_days == 5:
            print("Congrats! You got 2000 off on your journy.")
        elif how_many_days == 7:
            print("Congrats! You got 3000 off on your journy.")
        print("""Your Ticket and Id_card will be sent to you on text message in under a hour.""")
        # cab_book = input("Wanna book Cab.[yes or no]: ").lower
        # if cab_book == "yes":
        #     print("Ok we book a cab for you.")
        # else:
        #     print("It's ok ")
    else:
        print(f"We can't guide you with this {chd_bdgt} of budget.")


# Second option 

elif travel_places == 2:
    print("Cool! You wanna Skiing in Ladakh.")
    input_bdgt = int(input("tell me your budget:"))
    if input_bdgt < 10000:
        print(" you can try our low budget tour of Chandighar. ")
    else:
        print("u can travel with this budget")
        mean_of_trnsprt = input("How do you want to go?\nAirplane ✈️  or bus 🚎: ")
        if mean_of_trnsprt == "Airplane":
            print("We can provide a ticket for you:✈️")
        else:
            print("Ok! We can book a bus for you:🚎")
        how_many_days = int(input("How many days you wanna stay in hotel 🏨:"))
        if how_many_days < 5:
            print("OK then We booked a hotel 🏨 for You")
        elif how_many_days == 5:
            print("Congrats! You got 2000 off on your journy.")
        elif how_many_days == 7:
            print("Congrats! You got 3000 off on your journy.")
        print("""Your Ticket and Id_card will be sent to you on text message in under a hour.""")


# Third option

elif travel_places == 3:
    print("Namste ji! You want to see some Historical Places.")
    input_bdgt2 = int(input("tell me your budget:"))
    if input_bdgt2 < 10000:
        print("you can try our low budget tour of Chandighar.")
    else:
        print("u can travel with this budget ")
        mean_of_trnsprt = input("How do you want to go?\nAirplane ✈️  or bus 🚎: ")
        if mean_of_trnsprt == "Airplane":
            print("We can provide a ticket for you:✈️")
        else:
            print("Ok! We can book a bus for you:🚎")
        how_many_days = int(input("How many days you wanna stay in hotel 🏨:"))
        if how_many_days < 5:
            print("OK then We booked a hotel 🏨 for You")
        elif how_many_days == 5:
            print("Congrats! You got 2000 off on your journy.")
        elif how_many_days == 7:
            print("Congrats! You got 3000 off on your journy.")
        print("""Your Ticket and Id_card will be sent to you on text message in under a hour.""")

# Fourth option

elif travel_places == 4:
    print("Apperciate! Welcome to Silicon Valley of INDIA.")
    input_bdgt3 = int(input("tell me your budget:"))
    if input_bdgt3 < 10000:
        print("you can try our low budget tour of Chandighar.")
    else:
        print("u can travel with this budget ")
        mean_of_trnsprt = input("How do you want to go?\nAirplane ✈️  or bus 🚎: ")
        if mean_of_trnsprt == "Airplane":
            print("We can provide a ticket for you:✈️")
        else:
            print("Ok! We can book a bus for you:🚎")
        how_many_days = int(input("How many days you wanna stay in hotel 🏨:"))
        if how_many_days < 5:
            print("OK then We booked a hotel 🏨 for You")
        elif how_many_days == 5:
            print("Congrats! You got 2000 off on your journy.")
        elif how_many_days == 7:
            print("Congrats! You got 3000 off on your journy.")
        print("""Your Ticket and Id_card will be sent to you on text message in under a hour.""")


# solved all questions but not included cab services.
