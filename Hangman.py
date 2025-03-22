import random

logo = '''
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/
'''
stages = [
    '''    +------+
    |      |
    O      |
   /|\     |
   / \     |
        ---+---''',
    '''    +------+
    |      |
    O      |
   /|\     |
   /       |
        ---+---''',
    '''    +------+
    |      |
    O      |
   /|\     |
           |
        ---+---''',
    '''    +------+
    |      |
    O      |
   /|      |
           |
        ---+---''',
    '''    +------+
    |      |
    O      |
    |      |
           |
        ---+---''',
    '''    +------+
    |      |
    O      |
           |
           |
        ---+---''',
    '''    +------+
    |      |
           |
           |
           |
        ---+---'''
]

movies = [
    "The Godfather", "The Shawshank Redemption", "Schindler's List", "Pulp Fiction", "Forrest Gump",
    "The Dark Knight", "Inception", "Fight Club", "The Matrix", "Titanic",
    "The Lion King", "Toy Story", "Finding Nemo", "Up", "Coco",
    "Spirited Away", "Howl's Moving Castle", "Avengers: Endgame", "Harry Potter", "The Hunger Games"
]

def play_hangman():
    chosen_word = random.choice(movies).lower()
    l1 = list(chosen_word)
    l2 = ["_" if char != " " else " " for char in chosen_word]
    lives = 6

    print(logo)
    print(" ".join(l2))

    while "_" in l2 and lives > 0:
        guess = input("Guess a letter: ").lower()

        if guess in l1:
            for i in range(len(l1)):
                if l1[i] == guess:
                    l2[i] = guess
        else:
            lives -= 1

        print(" ".join(l2))
        print(stages[lives])

    if "_" not in l2:
        print("🎉 YOU WIN! 🎉")
    else:
        print(f"GAME OVER! The word was: {chosen_word.upper()}")

while True:
    play_hangman()
    replay = input("Do you want to play again? (y/n): ").lower()
    while replay not in ["y", "n"]:
        replay = input("Invalid input. Do you want to play again? (y/n): ").lower()
    if replay == "n":
        print("Thanks for playing! 🎭")
        break
