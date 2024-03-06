import random

current_round = 0
playing = False

def top_range(round):
  top_range = round * 2 + 1
  return top_range

def generate_random_number(max_numbers):
  random_number = random.randint(1, max_numbers)
  return random_number




while "yes" or "no" not in start_game:
  start_game = input("Would you like to play?\nYes or No: ").lower()
  if start_game == "yes":
    current_round += 1
    playing = True
    break 
  elif start_game == "no":
    print("Alright good bye g")
    break
  else:
    pass

while playing:
  number_list = top_range(round=current_round)
  random_number = generate_random_number(max_numbers=number_list)
  guess = None
  intro_guess = print(f"Guess a number between 1 and {number_list}")
  while guess != random_number:
    guess = int(input("Number: "))
    if guess == random_number:
      print("You won!")
      playing = False
      break
    elif guess > random_number:
      print("Go lower")
    elif guess < random_number:
      print("Go Higher")
    else:
      pass


