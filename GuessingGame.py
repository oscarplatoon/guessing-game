

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

