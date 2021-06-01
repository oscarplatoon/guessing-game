import random

class GuessingGame:


    def __init__(self):
        self.correct = random.randint(1,100)
        print('Welcome to guessing Game! Guess a random number between 1 - 100 has been generated!')
        self.guess_correct = False
        self.guess()

    def guess(self):
        while self.guess_correct == False:
            self.guess_number = int(input('Guess a number between 1-100: '))
            if self.guess_number == self.correct:
                print('You got it!')
                print('See you next time!')
                self.guess_correct = True
            elif self.guess_number > self.correct:
                print('Too High!')
            elif self.guess_number < self.correct:
                print('Too Low!')

game = GuessingGame()


            



