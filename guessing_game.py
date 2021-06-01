class GuessingGame():


    # init method or constructor 
    def __init__(self, num):
        self.number_to_guess = num
        self.slvd = False
   
    def guess(self, user_guess):
        if user_guess < self.number_to_guess:
            return 'low'
        elif user_guess > self.number_to_guess:
            return 'high'
        else:
            self.slvd = True
            return 'right'

    def solved(self):
        return self.slvd

import random

# ----- DRIVER CODE -----14

game = GuessingGame(random.randint(1,100))
last_guess  = None
last_result = None

while game.solved() == False:
    
    guess = 0
    while guess == 0:
        try:
            guess = int(input("Enter your guess: "))
        except: 
            print("Please enter a number from 1 to 100.")

    result = game.guess(guess)
    if result != 'right':
        print(f"Oops! Your last guess ({guess}) was {result}.")
        print("")
    
print(f"{guess} was correct!")




# game = GuessingGame(10)

# game.solved()   # => False

# game.guess(5)  # => 'low'
# game.guess(20) # => 'high'
# game.solved()   # => False

# game.guess(10) # => 'correct'
# game.solved()   # => True