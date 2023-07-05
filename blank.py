#This code converts words to blanks
def genrateBlank(word):
    ret=""
    for i in word:
        if i==" ":
            ret+=" "
        else:
            ret+="_"
    return ret

