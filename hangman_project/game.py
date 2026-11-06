
class HangmanGame:
    def __init__(self, word):
        self.word = word.lower()
        self.guessed_letters = []
        self.max_errors = 6
        self.errors = 0

    def display_progress(self):
        progress = []

        for letter in self.word:
            if not letter.isalpha() or letter in self.guessed_letters:
                progress.append(letter)
            else:
                progress.append("_")

        print("Progreso:", " ".join(progress))
        print("Letras adivinadas:", ", ".join(self.guessed_letters))
        print("Intentos restantes:", self.max_errors - self.errors)

    def guess_letter(self, letter):
        letter = letter.lower()

        if letter in self.guessed_letters:
            print("Ya adivinaste esa letra.")
            return

        self.guessed_letters.append(letter)

        if letter not in self.word:
            self.errors += 1
            print("Letra incorrecta.")
        else:
            print("¡Letra correcta!")

    def process_guess(self, letter):
        previous_errors = self.errors
        self.guess_letter(letter)
        return self.errors == previous_errors

    def is_won(self):
        for letter in self.word:
            if letter.isalpha() and letter not in self.guessed_letters:
                return False
        return True

    def is_lost(self):
        return self.errors >= self.max_errors

