import sys

# We declare the name for the output file where the results will be written
output_file = "output.txt"

def count_words(lines_in_file):
    # We create an empty dictionary to save the words and the number of times it appears in the text
    # As the words are not sorted in the text, using a dictionary with a key -> value relation is the
    # most efficient way to do it, as we can also search in the dictionary by the word itself and not
    # necessarely by index
    words_dic = {}

    for each_line in lines_in_file:
        # We select the words such as prepositions and conjuntions that we don't
        # to count during the process...
        discarded_special_chars = ['', '-', '&', '/']
        discarded_articles = ['el', 'la', 'los', 'las', 'un', 'uno', 'una', 'unos', 'unas', 'mi', 'mis', 'tu', 'tus', 'su', 'sus', 'nuestro', 'nuestros', 'vuestro', 'vuestros']
        discarded_prepositions = ['a', 'ante', 'bajo', 'cabe', 'con', 'contra', 'de', 'desde', 'en', 'entre', 'hacia', 'hasta', 'para', 'por', 'segun', 'sin', 'so', 'sobre', 'tras']
        discarded_conjunctions = ['y', 'e', 'ni', 'que', 'pero', 'aunque', 'sino', 'sea', 'pues', 'porque']
        # ... and we add all different arrays in a unique list of discarded
        # words (to avoid having to write again all of different arrays in the
        # if condition of the loop while checking words of the file one by one)
        discarded_words = discarded_prepositions + discarded_special_chars + discarded_articles + discarded_conjunctions

        # We split the words read and save them into a list
        words = each_line.split(' ')

        for each_word in words:
            # The method strip() returns a copy of the string in which all chars have been stripped from
            # the beginning and the end of the string. As no value is passed as argument, by default the
            # whitespace char is the one removed. The function lower() also converts all chars in the
            # string to lowercase so the program will not count as two different words those who start
            # uppercase for example in the beginning of a sentence:
            each_word = each_word.strip().lower()

            # If the word already exists in our dictionary as a key, we increment the counter by 1
            if each_word in words_dic:
                words_dic[each_word] += 1
            # Otherwise, we create a new entry in the dictionary and initialize it to 1...
            else:
                # ... only if the word is not in the discarded_words list
                if (each_word not in discarded_words):
                    words_dic[each_word] = 1

    # We open the output file where we are going to write and save the results
    f = open(output_file, 'w')

    # For each word stored in the dicitonary, we write the word itself (corresponding to the ley of the
    # dicitonary) and the number of times it appear (corresponding to the value attached to the key)
    for key, value in words_dic.items():
        f.write(key + ": " + str(value) + '\n')

    f.close()


if __name__ == "__main__":
    # As we are executing our code directly from Jupyter notebook, we have decided to comment the code
    # used to import the filename as a parameter in case we want to execute our program from the terminal,
    # using the sys module we import at the beginning of the code. The file from where our program read the
    # text to count its words must be called 'example.txt'

    # if len(sys.argv) == 2:
        # We try to open the file passed by argument
        # file_to_read = open(sys.argv[1])
        file_to_read = open('example.txt')

        if (file_to_read):
            # We read each line of the given file and save them in a list returned by the readlines() function
            lines_in_file = file_to_read.readlines()
            count_words(lines_in_file)
            print("The output file has been succesfully created.")

            file_to_read.close()
        else:
            print("The file does not exist.")
    # else:
        # print("Usage: python " + sys.argv[0] + " filename")
