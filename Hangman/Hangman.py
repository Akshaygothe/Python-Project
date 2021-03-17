import random
from words import words

def get_valid_word(words):
    word = random.choice(words) #Randomly choosing a word from list.
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet_list = [] #converting word_letters in upper case.
    for i in word_letters:
        j = i.upper()
        alphabet_list.append(j)
    #print(alphabet_list)
    alphabet = set(alphabet_list) # converting alphabet_list in set.
    #print(alphabet)
    used_letters = set() #what the user has guessed
    show_letters = set() #program will show random word to user. It will make this game easy.
    # if lenght of word is <= 3, show 1 letter.
    # if length of word is <= 5, show 2 letters.
    # if length of word is <= 8, show 3 letters.
    if len(word) <= 3:
        show_letters.add(random.choice(word))
    elif len(word) > 3 and len(word) <= 5:
        for i in range(2):
            x = random.choice(word)
            while x in show_letters:
                x = random.choice(word)
            show_letters.add(x)
    elif len(word) > 5 and len(word) <= 8:
        for i in range(3):
            x = random.choice(word)
            while x in show_letters:
                x = random.choice(word)
            show_letters.add(x)
    else:
        for i in range(4):
            x = random.choice(word)
            while x in show_letters:
                x = random.choice(word)
            show_letters.add(x)

    for i in show_letters:
        word_letters.remove(i)
    
    lives = 6 # we are providing user 6 wrong chances.


    # getting user input
    while len(word_letters) > 0 and lives > 0:
        
        #print('used_letters:', used_letters)
        # letters used
        print('You have',lives,'lives left. and You have used these letters:',' '.join(used_letters))

        word_list = []
        for letter in word:
            if letter.upper() in used_letters or letter in show_letters:
                word_list.append(letter)
            else:
                word_list.append('-')
        #print('word List:', word_list)
#        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('current word:', ' '.join(word_list))
        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet:
            if user_letter in used_letters:
                print('Letter is already used.')
            else:
                used_letters.add(user_letter)
                if user_letter.lower() in word_letters:
                    word_letters.remove(user_letter.lower())
            

        else:
            lives = lives - 1 # takes away life if user is wrong.
            print('Letter is not in word.')

        used_letters.add(user_letter)

    if lives == 0 and len(word_letters) != 0:
        print('You died, Sorry. The word was', word)
    else:
        print('You guessed the word correctly', word)


if __name__ == "__main__":
    hangman()
