# a game of higher or lower using instagram followers
import art
from replit import clear
from game_data import data
import random

def format_data(account):
  """format the account data into printable format."""
  account_name = account_a["name"]
  account_descr = account_a["description"]
  account_country = account_a["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
  """take the user guess and follower counts and returns if they got it right"""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"
  
# display art 
print(art.logo)
score = 0

# make the game repeatable.
game_should_continue = True
# making account at position B become the next account at position A
account_b = random.choice(data)
while game_should_continue:
  # generate a random account from the game data
  account_a = account_b
  account_b = random.choice(data)
  while account_a == account_b:
    account_b = random.choice(data)
  
  # format the account data into printable format.
  print(f"Compare A: {format_data(account_a)}.")
  print(art.vs)
  print(f"Against B: {format_data(account_b)}.")
  
  # ask user for a guess.
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  # check if user is correct.
  ## get follower count of each account.
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  ## use if statement to chek if user is correct.
  is_correct = check_answer(guess, a_follower_count, b_follower_count)
  # clear the screen
  clear()
  print(art.logo)
  
  # give user feedback on their guess
  if is_correct:
    # score keeping
    score += 1
    print(f"You're right! Current score: {score}.")
  else:
    game_should_continue = False
    print(f"Sorry, that's wrong, Final score: {score}.")
