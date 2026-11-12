import random
number = random.randint(1,50)
lives = 7
choice =[]
while lives >0:
  guessed = int(input("please guess a number:"))
  if guessed in choice:
    print("You already guessed that number!")
    print(lives)
  else:
    choice.append(guessed)
    if guessed>number:
      lives-=1
      print("too high")
      print(lives)
    elif guessed<number:
      lives-=1
      print("too low!")
      print(lives)
    else:

      print("correct")
      break
if lives==0:

  print("GAME OVER")
