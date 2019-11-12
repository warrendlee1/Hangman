import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'
word_list = ['awkward','hello','hang']

def hangman():
    homepage()

    word = list(word_list[random.randint(0,len(word_list)-1)])
    hide_word = list("_"*len(word))
    print hide_word

    counter = len(word)

    while counter != 0:
        guess = raw_input("enter one letter: ")
        for i in range(len(word)):
            if guess == word[i]:
                hide_word[i] = word[i]
                counter -= 1
        print hide_word
    print "congrats"


    
def homepage():
    title = """
    █  █ █▀▀█ █▀▀▄ █▀▀▀ █▀▄▀█ █▀▀█ █▀▀▄ 
    █▀▀█ █▄▄█ █  █ █ ▀█ █ ▀ █ █▄▄█ █  █ 
    ▀  ▀ ▀  ▀ ▀  ▀ ▀▀▀▀ ▀   ▀ ▀  ▀ ▀  ▀ 
       W  A  R  R  E  N     L  E  E
    """

    print(title)

hangman()