import random
import sys
import hangman_art
import hangman_words

word_list = hangman_words.word_list
random_number = random.randint(0, len(word_list) - 1)
guessed_word = word_list[random_number]
length = len(guessed_word)

print(guessed_word)
print(hangman_art.logo)

blank = []


for i in range(length):
    blank += "_"
    
count = 0
life = len(hangman_art.stages) - 1

while  life >= 0:
    guess = input("Guess the letter: ")
    guess = guess.lower()
    for position in range(length):
        if guess == guessed_word[position]:
            blank[position] = guess
            print(f"{' '.join(blank)}")
            print(hangman_art.stages[life])
            if count == len(blank) - 1:
                print("YOu Won")
                sys.exit() # Terminate the entire program
            count += 1

    else:
        print(f"{' '.join(blank)}")
        print(hangman_art.stages[life])
        life -= 1
        if life == -1:
            print("You Lose")
