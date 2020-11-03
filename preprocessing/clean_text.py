import re
import string
from nltk.tokenize import word_tokenize


def return_dictionary():
    pattern = re.compile("<(/)?a[^>]*>")

    f = open('./test.txt', 'r', encoding='utf8')
    o = open('./temp', 'w', encoding='utf8')
    content = f.read()
    content = str(content)
    content_new = re.sub(pattern, "", content)

    # Replaces punctuations with spaces
    translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))

    # Removes weird punctuations
    content_new = content_new.translate(translator)
    content_new=content_new.translate(str.maketrans('', '', "‘’’"))

    # Makes all text lower case
    content_new = content_new.lower()

    # Creating a dictionary of words in the documents
    # Will be used later

    processed_text = word_tokenize(content_new)
    dictionary = set(processed_text)
    # print(dictionary)
    # print(len(dictionary))

    o.write(content_new)
    f.close()
    o.close()
    return dictionary
