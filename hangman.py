import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'
word_list = ['awkward','hello','hang']

def hangman():
    homepage()

    word = list(word_list[random.randint(0,len(word_list)-1)])
    hide_word = list("_"*len(word))
    print (" ".join(hide_word))

    counter = len(word)

    while counter != 0:
        guess = raw_input("""
        
        enter one letter: """)
        for i in range(len(word)):
            if guess == word[i]:
                hide_word[i] = word[i]
                counter -= 1
        print (" ".join(hide_word))
    print """
        C O N G R A T S !
    """


    
def homepage():
    title = """
  [  H   A   N   G       M   A   N  ]

        w a r r e n   l e e
    """

    print(title)

hangman()