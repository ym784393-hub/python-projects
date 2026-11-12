items = []
prices = []
print("\n **** welcome to ishop calculator *****")
number= int(input("How many items are there in your basket today?  "))
if number > 0:
    print("\n let's get to counting them ...")
    for i in range(0, number):
        name=input(f"please tell me the name of the item number {i+1} ...")
        items.append(name)
        price=float(input(f"what is the price of {name} \n$ "))
        prices.append(price)
    choice = input("would you like to see your entire basket items?  ").lower()
    if choice == "yes":
        print(items)
        see_price = input("would you like to see how much it'll cost?  ").lower()
        if see_price == "yes":
            print("\nBuying these items will cost: ")
            print(sum(prices))

        else:
            input("press enter to exit")
    else:
        input("press Enter to exit")
else:
    print("seems like you're not in the mood for shopping today")
