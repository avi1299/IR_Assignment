from clean_text import return_dictionary


def term_frequency(doc_path):
    """
    Computes term frequency for a document
    :param doc_path: path to the individual document
    :return: term frequency key value pair
    """
    f = open(doc_path, 'r', encoding='utf8')
    doc = f.read()
    doc = str(doc)
    doc = doc.split(" ")
    vocab = return_dictionary()
    word_dict = dict.fromkeys(doc, 0)
    for word in doc:
        word_dict[word] += 1
    return word_dict


Dict = term_frequency('./temp')
print(Dict)
