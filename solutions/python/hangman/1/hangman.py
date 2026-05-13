# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.word = word
        self.masked = ["_"] * len(self.word)
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING

    def guess(self, char):
        guessed_correctly = False
        if self.status == STATUS_LOSE:
            raise ValueError("You've lost the game!")
        if self.status == STATUS_WIN:
            raise ValueError("The game is over, you won!")
        if self.remaining_guesses == 0:
            self.status = STATUS_LOSE
        for ix, ch in enumerate(self.word):
            if ch == char and char != self.masked[ix]:
                guessed_correctly = True
                self.masked[ix] = char
        if not guessed_correctly:
            self.remaining_guesses -= 1
        if self.word == self.get_masked_word():
            self.status = STATUS_WIN

    def get_masked_word(self):
        return "".join(self.masked)

    def get_status(self):
        return self.status
