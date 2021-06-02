
class GuessingGame():
    user_guess = False

    def __init__ (self, answer):
        self.answer = answer
    
    def guess(self, user_guess):
        print(self.answer)
        return False


# game = GuessingGame(10)

# game.solved()   # => False

# game.guess(5)  # => 'low'
# game.guess(20) # => 'high'
# game.solved()   # => False

# game.guess(10) # => 'correct'
# game.solved()   # => True