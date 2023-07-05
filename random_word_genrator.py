# This code selects and returns a Random Avenger Name
import random
def pick_random_word():
    ls=["Iron Man","Captain America","Hawk Eye","Black Widow","Thor","Ant Man","The Hulk","Super Man","Bat Man","Vision","Black Panther","Dr Strange"]
    word= ls[random.randint(0,len(ls)-1)]
    return word

