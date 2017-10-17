
# coding: utf-8

# Víctor Fernández Rubio
# David González Jiménez
# Carlos Llames Arribas
# Marta Pastor Puente

def word_cypher(text, shift_L):
    # We need to initialize the string variable
    semi_cyphered_text = ""

    for char in text:
        if char.isalpha():
            semi_cyphered_text += chr((ord(char) + (int(shift_L)) % 26))
            # if char.islower():
                # [a - z] ASCII corresponds to [97 - 122]
                #semi_cyphered_text += chr((ord(char) - 97 + int(shift_L)) % 26 + 97)
            # if char.isupper():
                # [A - Z] ASCII corresponds to [65 - 90]
                #semi_cyphered_text += chr((ord(char) - 65 + int(shift_L)) % 26 + 65)
        else:
            semi_cyphered_text += char
    return semi_cyphered_text



def sentence_cypher(text, shift_L, shift_W):
    full_cyphered_text = ""
    semi_cyphered_text = word_cypher(text, shift_L)

    # We save in 'words' variable a list of the words conforming the full text to cypher
    words = semi_cyphered_text.split(' ')

    # We slice the words list from the beginning to the end, producing a shallow copy...
    tmp_copy = words[:]
    #... and create an empty list where we will save the index of the word list to shift
    index = []

    # We traverse the words list to reorder them depending on the shift given as parameter
    for i in range(0, len(words)):
        # We add to the index list the position of the current word to be shifted...
        index.append((i + int(shift_W)) % len(words))
        #... and copy into the tmp_copy array the word in the position assigned to it after the shift
        tmp_copy[index[i]] = words[i]

    for j in range(0, len(tmp_copy) - 1):
        # We add all words saved in the tmp array to the string that will be shown to the user
        # Note that we do not use a blank space as separator but add it in the end instead to avoid
        # having a blank space at the beginning of the full_cyphered_text string
        separator = ""
        full_cyphered_text += separator.join(tmp_copy[j]) + " "

    # We add the last word to the full_cyphered_string without adding a blank space at the end
    full_cyphered_text += tmp_copy[len(tmp_copy) - 1]

    print ("\nCyphered text: " + full_cyphered_text)



if __name__ == "__main__":
    text = input("Text to cypher: ")
    shift_L = input("Letter shift (n): ")
    shift_W = input("Word shift (m): ")

    if shift_L.isdigit() and shift_W.isdigit():
        sentence_cypher(text, shift_L, shift_W)
    else:
        print ("Shift must be an integer.")
