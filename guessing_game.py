import random


class GuessingGame():
   def __init__(self, answer):
       self.answer = answer
       
   def guess(self, user_guess):
       last_guess = user_guess
       if self.answer > user_guess:
           return "low"
       elif self.answer < user_guess:
           return "high"
       return "correct"

   def solved(self):
       return self.answer == last_guess
       
# ----- DRIVER CODE -----
game = GuessingGame(random.randint(1,100))
last_guess  = None
last_result = None

while game.solved() == False:
  if last_guess != None: 
    print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
    print("")

  last_guess  = int(input("Enter your guess: "))
  last_result = game.guess(last_guess)


print(f"{last_guess} was correct!")