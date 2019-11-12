import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'
word_list = ['awkward','hello','hang']

def guess_letter():
    guess = raw_input("enter one letter : ")
    while len(guess) > 1:
        guess = raw_input("enter one letter : ")
    return guess

def choose_word():
    word_index = random.randint(0,len(word_list))
    word = word_list[word_index]
    return word

def checker():


def homepage():
    # title = """
    #     █  █  █▀▀█  █▀▀▄  █▀▀▀  █▀▄▀█  █▀▀█  █▀▀█ 
    #     █▀▀█  █▄▄█  █  █  █ ▀█  █ ▀ █  █▄▄█  █  █ 
    #     ▀  ▀  ▀  ▀  ▀  ▀  ▀▀▀▀  ▀   ▀  ▀  ▀  ▀  ▀ 
    #       W   A   R   R   E   N       L   E   E

        
    #     """
    title = "HANGMAN by warren lee"
    print(title)
    

def hangman():
    homepage()
    choose_word()



#guess letter
#choose word
#