'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) < 2: # if the word is less then two cha 
        return 0 # then we return 0
    elif word.find("th") != -1: # if "th" is found in word grab that index and set count to 1 
        found_index = word.find("th") # setting a variable "th"
        count = 1
        return count + count_th(word[found_index + 2:]) # return the list counting upwards starting with the second placement and going to the end of the list
    else:
        return 0
