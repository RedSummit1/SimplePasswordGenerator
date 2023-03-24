def passwordMaker(str1, str2):
    """The purpose of this function is to interlock two different strings with the same index to form a password and any remaining characters will be added to the end"""

    bigger_string = max((str1,str2)) # find the biggest strings and smallest stirng (the smallest string being the limiting factor)
    smaller_string = min((str1, str2))
    password = "".join(("".join(element) for element in zip(str1, str2))) # took zip object and took each tuple and formed a string with each, then joined those strings and formed password
    if(len(bigger_string) * 2 != len(password)): # just incase str1 and 2 were the same size, only wanted to add if it was nessecary
        password += bigger_string[((len(smaller_string)) - len(bigger_string))::]
    return password

word1 = input("What is the first string? ")
word2 = input("What is the second string? ")
print(passwordMaker(word1, word2))

if __name__ == "__main__": 
