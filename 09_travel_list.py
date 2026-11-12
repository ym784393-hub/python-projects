travel_list=input("please type the names of the countries separated by a comma :....")
rrr=travel_list.split(", ")
for names in rrr:
   print("\n" + names + "\n")
   visited=input(f"have you ever visited {names} before ? yes \ No ....").lower()
   if visited == "yes":
     print("I hope you had a wonderfull time \n")
   else:
     print("I hope you get to visit it soon \n")
   print("--------------")
input("press enter to exit ....")
