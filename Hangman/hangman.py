import time
import random

HANGMAN_PICS = ['''
         +---+
             |
             |
             |
            ===''', '''
         +---+
         O   |
             |
             |
            ===''', '''
        +---+
        O   |
        |   |
            |
           ===''', '''
        +---+
        O   |
       /|   |
            |
           ===''', '''
        +---+
        O   |
       /|\  |
            |
           ===''', '''
        +---+
        O   |
       /|\  |
       /    |
           ===''', '''
        +---+
        O   |
       /|\  |
       / \  |
           ===''']


def word_chooser(all_words):
    random_word = random.choice(all_words)
    return random_word


def start_game(HANGMAN_PICS):
    all_words = open("all_words.txt", "r")
    all_words = word_reader()
    while True:
        random_word, level, yes_or_no, letter= "", None, "", None

        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        while level not in ["1", "2", "3"]:
            level = input("Please enter the difficulty level:")
            if level not in ["1", "2", "3"]:
                print("Out of given difficulties. Please try again.")
        print("\n\n")
        if level == "1":
            while len(random_word) > 5 or len(random_word) < 4:
                random_word = word_chooser(all_words)
        elif level == "2":
            while len(random_word) > 7 or len(random_word) < 6:
                random_word = word_chooser(all_words)
        else:
            while len(random_word) > 10 or len(random_word) < 8:
                random_word = word_chooser(all_words)
        print(random_word)
        random_word = list(random_word)
        word = ["__ "] * len(random_word)
        rights, y = 7, 0
        entered_index = []
        while letter != random_word and rights > 0:
            if len(entered_index) != len(random_word):
                letter = input("Enter the word or any character of the word:")
            while len(letter) !=1:
                print("You can only enter 1 character or all the word.")
                letter = input("Enter the word or any character of the word:")
            if letter == random_word or len(entered_index) == len(random_word):
                print("Congratulations. You have known the word. ^_^")
                for x in range(len(word)):
                    word[x] = list(random_word[x])
                break
            elif letter in random_word and random_word.index(letter) not in entered_index:
                print("Well done!. This character is in the chosen word.", rights, " rights remained.")
                word[random_word.index(letter)] = letter
                entered_index.append(random_word.index(letter))
                random_word[random_word.index(letter)] = ""
            else:
                rights -= 1
                if rights != 0:
                    print("This character is not in the chosen word. ", rights, " rights remained.")
                print(HANGMAN_PICS[y])
                y += 1
            if letter != random_word and rights != 0 or y <= 7 and rights != 0:
                for x in range(len(random_word)):
                    print(word[x], end=" ")
            print("\n\n")
        if rights == 0:
            print("Your rights are over.")
        yes_or_no = input("Do you want to continue to play?(y/n):")
        while yes_or_no not in ["Y", "y", "N", "n"]:
            print("Please enter the valid character.")
            yes_or_no = input("Do you want to continue to play?(y/n):")
        if yes_or_no in ["Y", "y"]:
            pass
        else:
            break


def word_reader():
    all_words = open("all_words.txt", "r")
    all_words = all_words.read().split("\n")
    return all_words


def main():
    print("Welcome to the Hangman game." + "\n")
    time.sleep(3)
    start_game(HANGMAN_PICS)


main()
