
def bomma(display):
    for i in display:
        print(i, end=" ")

import hangman_art_work
import hangman_words_list
Stages=hangman_art_work.stages
print(hangman_art_work.logo)
word_list = hangman_words_list.Word_list
import random

chosen_word = random.choice(word_list)
print(f'the solution is {chosen_word}.')
display = ["_"] * len(chosen_word)
lives = 6

while lives > 0 and "_" in display:
    guess = input("Guess a letter: ").lower()
    
    count = 0
    if(guess in display):
            print(f"You have already guessed {guess}")
            
    else:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
                count += 1
        if (count > 0):
              bomma(display)
              print(Stages[lives])
        else:
            print(f"you a guessed {guess},that's not in the word,You lose a life")
            bomma(display)
            lives -= 1
            print(Stages[lives])
if ("_" not in display):
    print("you won")
else:
    print("you lose")
