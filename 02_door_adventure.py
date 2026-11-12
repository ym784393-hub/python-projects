print("welcome to our app")
print(" there are two doors in front of you a red and a blue door")
door= input("wich door do you want to open\n").lower()


if door=="red":
    print ("Great! now you enter red a room\n you found three boxes (white), (black),(green),")
    boxes= input ("wich box do you open  \n").lower()
    if boxes=="white":
        print("oops! you opened a box filed with snaks ~~~")
    elif boxes== "green":
        print("congratulations! you found the treasure!$$$")
    elif boxes =="black":
        print ("Oops! you opened a box filed with spiders!@@@")
    else:
        print ("invalid choice")
elif door== "blue":
    print("Oops! you choice the crocoile door\n Game over~~~~")
else:
    print ("invaild choice!")
