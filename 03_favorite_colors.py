best=[]
color=input("add the first color you like\n")
best.append(color)
choice=input("Do you want to add more color? yes or No\n").lower()
if choice=="yes":
   color=input("add another color the list\n")
   best.append(color)
   print("the colors you like are")
   print(best)
else:
    print("the color you like is")
    print(best)
