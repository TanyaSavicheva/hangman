from curses.ascii import isalnum, isalpha
from enum import unique
from gettext import find
from operator import index
from pickle import FALSE, TRUE
from posixpath import isabs
import random
from tkinter import E, W
from tracemalloc import start
from turtle import right
from unicodedata import numeric

hangman = (
"""
_____________________________
                             |                                                                              
  ________         _____     |  
 |        |       /\ - -\    |
 |               /__\_-_-\   |  
 |               |  |    |   |
 |               |  | [] |   |  
 |               |__|____|   |                                                
 -                           |
_____________________________|
""",
"""
_____________________________
                             |                                                                              
  ________         _____     |  
 |        |       /\ - -\    |
 |        o      /__\_-_-\   |  
 |               |  |    |   |
 |               |  | [] |   |  
 |               |__|____|   |                                                
 -                           |
_____________________________|
""",
"""
_____________________________
                             |                                                                              
  ________         _____     |  
 |        |       /\ - -\    |
 |        o      /__\_-_-\   |  
 |        |      |  |    |   |
 |        |      |  | [] |   |  
 |               |__|____|   |                                                
 -                           |
_____________________________|
""",
"""
_____________________________
                             |                                                                              
  ________         _____     |  
 |        |       /\ - -\    |
 |        o      /__\_-_-\   |  
 |       \|      |  |    |   |
 |        |      |  | [] |   |  
 |               |__|____|   |                                                
 -                           |
_____________________________|
""",
"""
_____________________________
                             |                                                                              
  ________         _____     |  
 |        |       /\ - -\    |
 |        o      /__\_-_-\   |  
 |       \|/     |  |    |   |
 |        |      |  | [] |   |  
 |               |__|____|   |                                                
 -                           |
_____________________________|
""",
"""
_____________________________
                             |                                                                              
  ________         _____     |  
 |        |       /\ - -\    |
 |        o      /__\_-_-\   |  
 |       \|/     |  |    |   |
 |        |      |  | [] |   |  
 |       /       |__|____|   |                                                
 -                           |
_____________________________|
""",
"""
_____________________________
                             |                                                                              
  ________         _____     |  
 |        |       /\ - -\    |
 |        o      /__\_-_-\   |  
 |       \|/     |  |    |   |
 |        |      |  | [] |   |  
 |       / \     |__|____|   |                                                
 -                           |
_____________________________|
"""
)
max_wrong = len(hangman) - 1 #длина
GREEN = '\033[92m'
ENDC = '\033[0m' #закончить цвет

def get_word(file):
    words = open(file, 'r')
    words = words.read().split('\n')
    return random.choice(words)

def play(word):
    #word = get_word('words.txt') #слово, которое нужно будет угадывать
    #print(word)
    #one_letter = "[?]" * len(word) #по oдному дефису на каждую букву, которую нужно отгадать
    wrong = 0 #количество ошибок
    used = [] #буквы, которые уже отгадали
    right_suggested = []

    while wrong < max_wrong and sorted(right_suggested) != sorted(''.join(set(word))): #and one_letter != word: #не равно
        print(GREEN + hangman[wrong] + ENDC)
        print("\n`Used letters`\n", used)
        
        #hello-opw
        #hop

        for pos,char in enumerate(word):
            if(char in used):
                print(" " + word[pos], end=" ")
            elif (word[pos] == "-"):
                print(" - ", end="")
            else:
                print(" _ ", end="")

        #Печать слова

        #то что я ввожу в консоле
        guess = input("\n\nGuess a letter: ") #ввод

        #while guess in used:
            #print("You already used this letter: ", guess)
            #guess = input("\n\nGuess the letter: ")
        #проверяю наличие буквы в слове
        #new = ""
        if len(guess) != 1 or not isalpha(guess):
            print("Unexpected char")

        elif guess in word and guess not in used:
            print("\You are right! The letter", guess, "is in the word")
            used.append(guess)
            right_suggested.append(guess)
            
        elif guess in used:
            print("\You already used this letter")

            #for letter in range(len(word)): #если буква в списке
                #if guess == word[letter]:
                    #new += guess #прибавит к списку
                #else:
                    #new += one_letter[letter]
            #one_letter = new
        else:
            print("\nThe letter", guess, "is`n in word.")
            wrong += 1
            used.append(guess)

        #добавляю один элемент в конец списка
    
    #завершение игры
    if wrong == max_wrong:
        print(hangman[wrong])
        print("\nYou lost")
    else:
        print("\nYou won!")
    print("\nThe answer was", word)

def main():
    word = get_word('words.txt')
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word('words.txt')
        play(word)

if __name__ == "__main__":
    main()