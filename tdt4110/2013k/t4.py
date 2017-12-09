from random import randint
"""
Oppagve 4
"""

"""
Oppgave 4a (5%)
"""
def enter_words() -> [str]:
    words = []
    while True:
        word = input("Enter word [press Enter to quit]: ")
        if word == "":
            break
        # Task probably asks for:
        # words.append(word)
        # But the following syntax allows for you to enter more words per line!
        words.extend(word.split(" "))
    return words

"""
Oppgave 4b (10%)
"""
def no_vowels(in_list: [str]) -> [str]:
    vowels = list("aeiouy")
    out_list = []
    for word in in_list:
        word = list(word)
        for j, letter in enumerate(word):
            if letter.lower() in vowels:
                word[j] = ""
        out_list.append("".join(word))
    return out_list

"""
Oppgave 4c (10%)
"""
def random_sequence(list_one: [str], list_two: [str]) -> ([str], [str]):
    new_list_one = []
    new_list_two = []
    for i in range(len(list_one)):
        index = randint(0, len(list_one)-1)
        new_list_one.append(list_one.pop(index))
        new_list_two.append(list_two.pop(index))
    return new_list_one, new_list_two

"""
Oppgave 4d (5%)
"""
def print_newlines(amount: int):
    print("\n"*amount, end="")

"""
Oppgave 4e (10%)
"""
def play_game(answers: [str], puzzles: [str]) -> int:
    points = 0
    for i in range(len(puzzles)):
        print("Puzzle word: {}".format(puzzles[i]))
        guess = input("Guess word? ")
        if guess.lower() == answers[i].lower():
            print("You answered correctly!")
            points += 1
        else:
            print("You answered incorrectly! The Answer should be {}".format(answers[i]))
    return points

"""
Oppgave 4e (10%)
"""
def init_game():
    """
    Play a game of The NoVowels Game in the console.
    """
    print("The NoVowels Game")
    print("="*35)
    print("Player 2: Look away from the screen")
    print("Player 1: Write in a list of English words")

    word_list = enter_words()
    no_vowel_list = no_vowels(word_list)
    answers, quizzes = random_sequence(word_list, no_vowel_list)

    print_newlines(50)
    print("Player 2: Guess words that lack all vowels:")

    points = play_game(answers, quizzes)
    print("You've got {} of {} points".format(points, len(answers)))

def main():
    init_game()

if __name__ == "__main__":
    main()
