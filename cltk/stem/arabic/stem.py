"""Arabic Classical Stemmers module version Beta"""

from cltk.stem.arabic.assem_stemmer import AssemStemmer
from cltk.stem.arabic.khoja_stemmer import KhojaStemmer
from cltk.stem.arabic.tashaphyne_stemmer import TashaphyneStemmer
from cltk.stop.arabic.stopword_filter import stopwords_filter

__authors__ = ['Lakhdar Benzahia, <lakhdar.benzahia@gmail.com>']
__license__ = 'MIT License. See LICENSE.'

class ArabicStemmer:
    """
    Arabic Stemmers module

    """

    def __init__(self, stemmer):
        """Take stemmer name as argument to the class. Check availability and
        setup class variables."""
        self.stemmer = stemmer
        self.available_stemmers = ['AssemStemmer', 'KhojaStemmer', 'TashaphyneStemmer']
        assert self.stemmer in self.available_stemmers, \
            "Specific stemmer not available for '{0}'. Only available for: '{1}'.".format(self.stemmer,  # pylint: disable=line-too-long
                                                                                            self.available_stemmers)  # pylint: disable=line-too-long
    def stem(self, token):
        if self.stemmer == "AssemStemmer":
            assem_stemmer = AssemStemmer()
            stemmed = assem_stemmer.stem(token)
        elif self.stemmer == "KhojaStemmer":
            khoja_stemmer = KhojaStemmer()
            stemmed = khoja_stemmer.stem(token)
        elif self.stemmer == "TashaphyneStemmer":
            tashaphyne_stemmer = TashaphyneStemmer()
            stemmed = tashaphyne_stemmer.stem(token)

        return stemmed

    def stem_text(self, text):

        if self.stemmer == "AssemStemmer":
            filtered_tokens =  stopwords_filter(text)
            assem_stemmer = AssemStemmer()
            stems = []
            for token in filtered_tokens:
                stem = assem_stemmer.stem(token)
                stems.append(stem)
        elif self.stemmer == "KhojaStemmer":
            filtered_tokens = stopwords_filter(text)
            khoja_stemmer = KhojaStemmer()
            stems = []
            for token in filtered_tokens:
                stem = khoja_stemmer.stem(token)
                stems.append(stem)
        elif self.stemmer == "TashaphyneStemmer":
            filtered_tokens = stopwords_filter(text)
            tashaphyne_stemmer = TashaphyneStemmer()
            stems = []
            for token in filtered_tokens:
                stem = tashaphyne_stemmer.stem(token)
                stems.append(stem)
        return stems
