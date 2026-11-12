import random

rock_ascii = """
      _ _ _ _ _ _ _
_ _ _,   _ _ _ _ )
        (_ _ _ _ _)
        (_ _ _ _ _)
        (_ _ _ _ )
 ---._ _(_ _ _)
"""

paper_ascii = """
      _ _ _ _ _
_ _ _'
        _ _ _ _)_ _ _
          _ _ _ _ _ __)
          _ _ _ _ _ ___)
        _ _ _ _ _ _ _ )
---._ _ _ _ _ _ _ _)
"""

scissors_ascii = """
        -------
---'      _ _ _)_ _ _
              _ _ _ __)
          _ _ _ _ _ _ _)
          (_ _ _ _)
 ---._ _ _(_ _ _)
"""

print("\nWelcome to the Rock, Paper, Scissors game:")
confirm = input("Press enter to continue or type (help) for the rules... ").lower()

if confirm == "help":
    print("""
         ******** Rules ********
         1) You choose and the computer chooses
         2) Rock smashes scissors -> Rock wins
         3) Scissors cut paper -> Scissors win
         4) Paper covers rock -> Paper wins
         """)

user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

# Make the list all lowercase
if user_choice not in ["rock", "paper", "scissors"]:
    print("Invalid choice. Please run the program again and choose rock, paper, or scissors.")
else:
    # User's choice
    if user_choice == "rock":
        print(f"\nYou chose:\n{rock_ascii}")
    elif user_choice == "paper":
        print(f"\nYou chose:\n{paper_ascii}")
    else:
        print(f"\nYou chose:\n{scissors_ascii}")

    # Computer's choice
    computer_choice = random.choice(["rock", "paper", "scissors"])

    if computer_choice == "rock":
        print(f"\nComputer chose:\n{rock_ascii}")
    elif computer_choice == "paper":
        print(f"\nComputer chose:\n{paper_ascii}")
    else:
        print(f"\nComputer chose:\n{scissors_ascii}")

    # Decide the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print(f"You win! {user_choice} beats {computer_choice}.")
    else:
        print(f"You lose! {computer_choice} beats {user_choice}.")
