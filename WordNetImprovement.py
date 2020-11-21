from nltk.corpus import wordnet as wn


class WordNetImprovement:
    def __init__(self, query_term):
        self.term = query_term

    def extract_hypernyms(self):
        """
        Method to extract hypernyms of a query term
        :return: returns a dictionary with a list of hypernyms under contexts
        """
        temp = {}
        contexts = {}
        # Iterating though all synsets of a term, each having different contexts
        for i, element in enumerate(wn.synsets(self.term)):
            # Extracting hypernyms corresponding to the first and most common context
            temp = element.hypernyms()[0].lemma_names()
            contexts[i] = temp
        return contexts

    def extract_synonyms(self):
        """
        Method to extract synonyms of a query term
        :return: returns a dictionary with a list of synonyms under contexts
        """
        temp = {}
        contexts = {}
        # Iterating though all synsets of a term, each having different contexts
        for i, element in enumerate(wn.synsets(self.term)):
            # Extracting synonyms corresponding to the first and most common context
            temp = element.lemma_names()
            contexts[i] = temp
        return contexts
