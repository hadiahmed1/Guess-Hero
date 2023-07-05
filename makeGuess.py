# This code asks the user to make a guess,
def guess(word,ans):
    g=input("Enter an alphabet:")
    ret=""
    for i in range(0,len(word)):
        if g==word[i]:#if guess is correct
            ret+=word[i]#replace blank with guess
        else:
            ret+=ans[i]
    return ret