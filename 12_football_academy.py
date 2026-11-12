print("""
       **** Welcome to our Football Academy! ⚽****
        Our academy is dedicated to helping young players develop their football skills, build confidence, and reach their full potential through professional training and a supportive environment.
    """)
old=input("Is your child over 4 years old? (yes, or No, )\n").lower()
if old == "yes":
    print("\nYes! Your child can join our football academy. ⚽🎉")
    name=input("\nWhat is your child's name?: ")
    age= int(input("\nHow old is your child?: "))
    phone=input("\nplease type your phone number: ")
    adress=input("\nWhat is your home address?: ")
    print("\nThe academy membership fee is [250 EGP], and the football kit costs [300 EGP]. ⚽")

    choice =input("\nHas your child played football before? ⚽ (yes, No,) : ").lower()
    if choice == "no":
        print("\nYour child will start with us from the basics, step by step, and develop their football skills along the way. ⚽")
    elif choice == "yes":
        print("Great! Please visit our academy for an assessment to determine your child level. ")
    else:
        print("invaild choose!")
elif old == "no":
    print("Sorry, your child is not old enough to join our academy yet. ⚽")
else:
    print("invaild choose!")
