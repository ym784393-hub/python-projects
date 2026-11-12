import random
print("welcome to 'whose wallet?")
print("you will give me a list of names, and I will pick a person to pay ")
names= input ("If you're ready, enter the names seapareted by a comma ").split(", ")
print(f"please ask {random.choice(names)} to take out his wallet, dinner is on him.")
