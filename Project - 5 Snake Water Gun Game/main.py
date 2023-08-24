# Creating a snake, water and gun game--\

import random


# Create a game function..!
def game(user_guess):

  # defind the modes 'snake','water','gun'...
  mode = (0, 1, 2)
  # defind computer choose randomly choice in mode.
  computer = random.choice(mode)
  print(f"Computer choose: {computer!r}")

  # if user and computer same output then tie game.
  if (user_guess == computer):
    print("Games Tie.! both players same choice.!")

  # if user won the game....
  elif (user_guess == 0 and computer == 1):
    print("You win.! Sanke beats Water.!")
  elif (user_guess == 1 and computer == 2):
    print("You win.! Water beats Gun.!")
  elif (user_guess == 2 and computer == 0):
    print("You win.! Gun beats Snake")

  # if user lose the game...
  elif (user_guess == 0 and computer == 2):
    print("You lose.! Gun beats Snake.!")
  elif (user_guess == 2 and computer == 1):
    print("You lose.! Water beats Gun.!")
  elif (user_guess == 1 and computer == 0):
    print("You lose.! Snake beats water.!")

  else:
    print("Invalid value.! Please Enter 0, 1 or 2.")


# IF __NAME__=="__MAIN__" RUNNING THIS FUNCTION CONTROL.!
if __name__ == "__main__":
  print("Welcome to  Snake, Water & Gun Game.!")
  while True:
    try:
      print(
        "\nPlease Enter your choice \n0 for 'Snake' \n1 for 'Water' \n2 for 'Gun'\n"
      )
      user_guess = int(input("Enter your choice $: "))

      # call the function..
      game(user_guess)
      play_again = input("\nDo you want to play again? (yes/no): ")
      if play_again != 'yes':
        break

    except:
      print("Invalid value try again.! Please Enter 0, 1 or 2.")

  print("Thanks for playing the Game.!")