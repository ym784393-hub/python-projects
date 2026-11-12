print("welcome you to funny kids Nursery")
print("give you child the start\n Admission open at funny kids nursery")
print("working Hours 8:00 AM -2:00 PM")
age=input("for children above 3 years of age type(yes) or (No),\n").lower()
if age=="yes":
    print("good! would you prefer the Arabic section or the language section")
    section=input("Arabic or language\n").lower()
    if section== "arabic":
        print("ok, this section costs 450 EGP")
        name=input("please enter your name\n")
        phone=input("Enter phone Number\n")
        age=input("students age\n")
        print("kindly visit the Nursery to have an assessment test,")

    elif section == "language":
        print("ok, this section costs 750 EGP")
        name=input("please enter your name\n")
        phone=input("Enter phone number\n")
        age=input("students age\n")
        print("kindly visit the Nursery to have an assessment test,")
    else:
        print("invalid choice")
elif age=="no":
    print("we are sorry , but we cant accept applications for children under 3 years of age")
else:
    print("invalid choice")
