import random
def read():
    #open the .txt and create a list with the words
    word=[]
    with open ('./archivos/words.txt',"r") as f:
        for line in f:
            word.append(str(line))
    return word


def RandomWord():
    #pick a random word
    Random_Word= random.choice(read())
    Random_Word= Random_Word.strip('\n')
    return Random_Word.upper()


def game(word):
    
    line_word = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print ('welcome to Hangman game')
    print(display_hangman(tries))
    print(line_word)
    print('\n')
    #conditions to init the game
    while not guessed and tries > 0:
        guess = input("please guess a letter or the word ").upper()
        #condicion to acept 1 letter
        if len(guess) ==1 and guess.isalpha():
            # condition when usser use a letter
            if guess in guessed_letters:
                print("you already guessed the letter", guess)
            # condition when the letter is not in the word    
            elif guess not in word:
                print(guess, "is not the letter.")
                tries -= 1 
                guessed_letters.append(guess) # add the letter to a list
                
            #condition when the letter is in the word
            else:
                print("good job", guess, "is the letter")
                guessed_letters.append(guess)
                word_as_list = list(line_word) #convert the number of characters in a list
                indices = [i for i, letter in enumerate(word) if letter == guess]
                #when a letter is the same make a list whit the position of the letter
                
                for index in indices:
                    word_as_list[index]=guess
                line_word = "".join(word_as_list)
                if "_" not in  line_word:
                    guessed = True
                print(indices)
                #Condition for a word with the same lenght of the word
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("you already guessed the word", guess)
            elif guess != word:
                print (guess,"is not the word")
                tries -=1
                guessed_words.append(guess)
            else:
                guessed = True
                line_word=word
        else:
             print("Not a valid guess.")
        print(display_hangman(tries))
        print(line_word)
        print("\n")
    if guessed:
        print ("congrats")
    else:
        print("you lose")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def run():
    word = RandomWord()
    game(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = RandomWord()
        game(word)
if __name__=='__main__':
    run ()
