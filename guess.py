#This is a guess the number game.

import random
print('hello, what is your name ?')
name = input()

secretNumber = random.randint(1 , 20)
print('well, ' + name + ', I am thinking of a number between 1 and 20.')

#print('Debug: Secret number is ' + str(secretNumber))
#Ask the player to guess 6 times.

for guessTaken in range(1, 7):
      print('Take a guess.')
      guess = int(input())
      
      if guess < secretNumber:
          print('your guess is too low.')
      elif guess > secretNumber:
          print('your guess is too high.')
      else:
          break #this condition is the correct guess!

if guess == secretNumber:
    print('good job, '+ name + '! you guessed my number in ' + str(guessTaken) +  ' guesses.')
else:
    print('nope,the number I was thinking was ' + str(secretNumber))
