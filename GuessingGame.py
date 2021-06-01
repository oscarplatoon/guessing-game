class GuessingGame():
    result_of_last_user_guess = False

    def __init__(self, answer):
        self.correctAnswer = answer
    
    def guess(self, user_guess):
        if (user_guess > self.correctAnswer):
            self.result_of_last_user_guess = False
            return "high"
        elif (user_guess < self.correctAnswer):
            self.result_of_last_user_guess = False
            return "low"
        else:
            self.result_of_last_user_guess = True
            return "correct"
    
    def solved(self):
        return self.result_of_last_user_guess
