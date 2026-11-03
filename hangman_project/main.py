def get_valid_guess(guessed_letters):
    while True:
        guess = input("Ingresa una letra: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Error: debes ingresar una sola letra.")
        elif guess in guessed_letters:
            print("Error: ya adivinaste esa letra.")
        else:
            return guess


if __name__ == "__main__":
    guessed_letters = []

    letter = get_valid_guess(guessed_letters)
    print("Letra válida:", letter)
