#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo

def setting_difficulty():
  """Asks for the difficulty ans sets the number of attempts (lives) accordingly."""
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard':   ").lower()
  while difficulty != "hard" and difficulty != "easy":
    difficulty = input("Unrecognized answer. Please type 'easy' or 'hard':   ")
  if difficulty == "hard":
    return 5
  if difficulty == "easy":
    return 10

play = "y"

while play == "y":
## Intro
  print(logo)
  print("Welcome to the Number Guessing game.")
  print("I'm thinking of a number between 1 and 100.")
  pc_choice = random.randint(1, 100)
  lives = setting_difficulty()
  game_over = False
## Input
  while lives > 0 and game_over == False:
    guess = int(input("Make a guess:   "))
## check
    if guess == pc_choice:
      print(f"Brilliant! It was indeed {pc_choice}. You guessed the number!")
      game_over = True
    elif guess < pc_choice:
      lives -= 1
      print(f"Too low. You now have {lives} attempts. ")
    elif guess > pc_choice:
      lives -= 1
      print(f"Too high. You now have {lives} attempts. ")
## lives 0
  if lives == 0:
    print(f"Oh no, you didn't find the right number. I chose {pc_choice}")

## play again?
  play = input("Do you want to play again? Y/N:   ").lower()
  while play != "y" and play !="n":
    play = input("Unrecognized choice. Do you want to play again? Type Y for 'yes', N for 'no':    ")