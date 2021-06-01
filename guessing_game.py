import random


class GuessingGame():
  #Variable holding amount of guesses from user
  guessesTaken = 0
  
  #Call on a function to choose a num 1 - 100
  secret_number = random.randint(1,100)
  
  #For loop to account for number of guesses
  for guessesTaken in range(13):
      #Store user's guess as an int
      guess = input('Guess a number between 1 and 20: ')
      guess = int(guess)
      
      #If statements for correct, too low, and too high guesses
      if guess < secret_number:
        print("Your guess is too low") 
      elif guess > secret_number:
        print("Your guess is too high.")
      else:
          break   

  if guess == secret_number:
    guessesTaken = str(guessesTaken + 1)
    print(f"You guessed my number in {guessesTaken} guesses!")     
  
  if guess != secret_number:
    number = str(secret_number)  
    print(f"No. The number was {secret_number}")
  
GuessingGame()
