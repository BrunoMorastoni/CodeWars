# DESCRIPTION:
# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.

# SOLUTION:
def get_count(sentence):
    vogal = ["a","e","i","o","u"]
    contador = 0
    
    for letra in vogal:
        cont = sentence.count(letra)
        contador += cont
    return contador