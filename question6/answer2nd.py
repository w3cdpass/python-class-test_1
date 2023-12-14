# Tax-calculate
whats_my_tax = int(input("Enter your tax:"))

if whats_my_tax < 900000:
    if whats_my_tax < 300000:
        print("no tax")
    elif whats_my_tax <= 300000:
        print("give me tax")
        tax20 = whats_my_tax * 20 / 100
        print(f"your {whats_my_tax} of 20% tax is {tax20}.")
    else:
        if whats_my_tax <= 500000:
            print("30% tax")
            tax30 = whats_my_tax * 30 /100
            print(f"{whats_my_tax} of 30% tax is {tax30}")
    
else:
    print("i'm calculating")
    tax40 = whats_my_tax * 40 /100
    print(f"{whats_my_tax} of 40% tax is {tax40}")
    