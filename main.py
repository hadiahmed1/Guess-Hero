
from random_word_genrator import pick_random_word
from blank import genrateBlank
from makeGuess import guess
from result import win_or_loose
def playGame(attempts=5):# default value of attempts=5, if no arguments re passed
    print("Guess The Avengers Name")
    word=pick_random_word()#picking a random word
    current_word=genrateBlank(word)#genraring blanks
    print(current_word)
    while(attempts!=0 and word!=current_word):
        g=guess(word, current_word)#guessing
        if g==current_word:#
            attempts-=1 #reducing attempts if wrong guess
        else:
            current_word=g#updating current word
        print(current_word,"   You hsve",attempts,"attempts left")
    win_or_loose(current_word,word)#checking whether the player won the game or not
    

if __name__=="__main__":
    playGame()