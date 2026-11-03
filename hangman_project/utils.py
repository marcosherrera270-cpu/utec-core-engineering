import random

def get_random_word():
    with open("wordlist.txt", "r") as file:
        words = [word.strip() for word in file if word.strip().isalpha()]

    return random.choice(words)
