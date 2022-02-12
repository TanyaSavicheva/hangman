import random

hangman = (
"""
1
""",
"""
2
""",
"""
3
""",
"""
4
""",
"""
5
""",
"""
6
""",
"""
7
"""
)
max_wrong = len(hangman) - 1 #длина

def get_word(file):
    words = open(file, 'r')
    words = words.read().split('\n')
    return random.choice(words)

word = get_word('words.txt') #слово, которое нужно будет угадывать
print(word)
one_letter = " ? " * len(word) #по oдному дефису на каждую букву, которую нужно отгадать
wrong = 0 #количество ошибок
used = [] #буквы, которые уже отгадали

while wrong < max_wrong and one_letter != word: #не равно
    print(hangman[wrong])
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
input("\n\nWould you like to play again?")