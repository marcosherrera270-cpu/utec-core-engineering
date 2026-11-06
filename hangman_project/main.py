from game import HangmanGame
from utils import get_random_word


def get_valid_guess(guessed_letters):
    while True:
        guess = input("Ingresa una letra: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Error: debes ingresar una sola letra.")
        elif guess in guessed_letters:
            print("Error: ya adivinaste esa letra.")
        else:
            return guess


def main():
    word = get_random_word()
    game = HangmanGame(word)

    print("¡Bienvenido al juego Hangman!")

    while not game.is_won() and not game.is_lost():
        game.display_progress()

        letter = get_valid_guess(game.guessed_letters)

        if game.process_guess(letter):
            print("¡Correcto!")
        else:
            print("Letra incorrecta.")

    if game.is_won():
        print("¡Felicidades! ¡Ganaste!")
    else:
        print("¡Perdiste! La palabra era:", word)


if __name__ == "__main__":
    main()
