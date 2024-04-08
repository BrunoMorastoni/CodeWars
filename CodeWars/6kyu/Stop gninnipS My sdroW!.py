# DESCRIPTION:
# Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

# Examples:

# "Hey fellow warriors"  --> "Hey wollef sroirraw" 
# "This is a test        --> "This is a test" 
# "This is another test" --> "This is rehtona test"

# SOLUTION:
def spin_words(sentence):
    
    lista_invertida = [] 
    sentence = sentence.split()
    
    for palavra in sentence:
        if len(palavra) >= 5:
            lista_invertida.append(palavra[::-1])

        else:
            lista_invertida.append(palavra)

    return ' '.join(lista_invertida)