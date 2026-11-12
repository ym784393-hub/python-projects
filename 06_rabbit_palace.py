print("welcome to palace the rabbit\n")
tree=[["*", "*", "*"],["*", "*", "*"],["*", "*" ,"*"]]

print(f"{tree[0]}\n{tree[1]}  \n{tree[2]}")
print("\nwhere should the rabbit go?  & ")

position=(input("please choose a row and a column "))
row=int(position[0])
column=int(position[1])

tree[row-1][column-1] = "&"

print("\n success .... \n")

print(f"{tree[0]}\n{tree[1]} \n{tree[2]}")
