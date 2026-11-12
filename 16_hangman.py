import random

# Words are lowercase from the start, to be safe
world = ["office", "joo", "apple", "strawberry"]
random_world = random.choice(world)

# Show underscores, one per letter of the word
display = ["_"] * len(random_world)

print(' '.join(display))

leaves = 6
choice = []
stages = [
    """
     +---+
     |   |
         |
         |
         |
    ========
    """,

    """
     +---+
     |   |
     O   |
         |
         |
    ========
    """,

    """
     +---+
     |   |
     O   |
     |   |
         |
    ========
    """,

    """
     +---+
     |   |
     O   |
    /|   |
         |
    ========
    """,

    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    ========
    """,

    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    ========
    """,

    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    ========
    """
]
while "_" in display and leaves > 0:
    guessed = input("please guess a letter: ").lower()
    if guessed in choice:
        print("You already guessed that letter!")
    else:
      choice.append(guessed)

    # If the letter is wrong, lose a life
      if guessed not in random_world:
          leaves -= 1
          print("You have", leaves, "lives left")
          print(stages[6 - leaves])

    # If the letter is right, reveal it in place of the underscore
      for position in range(len(random_world)):
          if random_world[position] == guessed:
              display[position] = guessed

    print(' '.join(display))
if "_" not in display:
    print("You win! 🎉")
else:
    print("You lose! 💀")
    print("The wors:", random_world)
