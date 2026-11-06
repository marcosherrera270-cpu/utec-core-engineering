class HangmanGame:
    def __init__(self, word):
        self.word = word
        self.guessed_letters = []
        self.max_errors = 6
        self.errors = 0

    def display_progress(self):
        progress = []

        for letter in self.word:
            if letter in self.guessed_letters:
                progress.append(letter)
            else:
                progress.append("_")

        print("Progreso:", " ".join(progress))
        print("Letras adivinadas:", ", ".join(self.guessed_letters))
        print("Intentos restantes:", self.max_errors - self.errors)

    def process_guess(self, letter):
        if letter in self.word:
            self.guessed_letters.append(letter)
            return True
        else:
            self.errors += 1
            return False

    def process_guess(self, letter):
        if letter in self.word:
            self.guessed_letters.append(letter)
            return True
        else:
            self.errors += 1
            return False
