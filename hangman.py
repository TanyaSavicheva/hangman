import random

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
    print(word)
    one_letter = "[?]" * len(word) #по oдному дефису на каждую букву, которую нужно отгадать
    wrong = 0 #количество ошибок
    used = [] #буквы, которые уже отгадали

    while wrong < max_wrong and one_letter != word: #не равно
        print(GREEN + hangman[wrong] + ENDC)
        print("\n`Used letters`\n", used)
        print("\nYour word:\n", one_letter) 
        #то что я ввожу в консоле
        guess = input("\n\nGuess a letter: ") #ввод
        while guess in used:
            print("You already used this letter: ", guess)
            guess = input("\n\nGuess the letter: ")
        used.append(guess) #добавляю один элемент в конец списка
        #проверяю наличие буквы в слове
        new = ""
        if guess in word:
            print("\You are right! The letter", guess, "is in the word")
            for letter in range(len(word)): #если буква в списке 
                if guess == word[letter]:
                    new += guess #прибавит к списку
                else:
                    new += one_letter[letter]
            one_letter = new
        else:
            print("\nThe letter", guess, "is`n in word.")
            wrong += 1
    
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