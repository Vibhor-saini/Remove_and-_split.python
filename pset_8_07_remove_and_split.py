Name = "vibhor is a good boy"
print(Name)

def remove_and_split(string, word):         # function declaration
    newStr = string.replace(word,"")        # (1)first step
    return newStr.strip()                   # (2) second step
                                     
r = remove_and_split(Name,"good")           # function call
print(r)


#  In the above program first we will replace the
#  word from the string (1) using  and then we will split
#  blank space using strip() function.