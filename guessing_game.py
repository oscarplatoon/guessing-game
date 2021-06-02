import random

class GuessingGame():
    last_guess = None

    def __init__ (self, answer):
        self.answer = answer

    def guess(self, user_guess):
        self.last_guess = user_guess

        if int(user_guess) == self.answer:
            return 'Correct'
        if int(user_guess) < self.answer:
            return 'Low'
        if int(user_guess) > self.answer:
            return "High"


    def solved(self):
        if self.last_guess == str(self.answer):
            return True
        else:
            return False

game = GuessingGame(random.randint(1,100))
last_guess  = None
last_result = None


while game.solved() == False:
    if last_guess != None: 
        print (last_guess)
        print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
        print("")
    
    last_guess  = input("Enter your guess: ")
    last_result = game.guess(last_guess)



print(f"{last_guess} was correct!")