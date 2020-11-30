import random 
from art import logo
print(logo)
print('Welcome to the number guessing game')
print('I\'m thinking of a number between 1 and 100')
number = random.randint(1,100)
difficulty = input('Choose a difficulty, Easy or Hard').lower()
if difficulty == 'easy':
  print('You have 10 guesses')
  lives = 10
elif difficulty == 'hard':
  print('You have 5 guesses')
  lives = 5
guess = int(input('Make a guess'))
while lives > 1:
  if guess == number:
    print('You won!')
    break
  elif guess < number:
    print('Too low')
    lives -= 1
    print(f'You have {lives} guesses left')
    guess = int(input('Make a guess'))

  elif guess > number:
    print('Too high')
    lives -= 1
    print(f'You have {lives} guesses left')
    guess = int(input('Make a guess'))
if guess != number:
  print('You lost!')
