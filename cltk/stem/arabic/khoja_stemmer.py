""" Khoj's stemmer for Classical Arabic """

from cltk.corpus.arabic.alphabet import *
from cltk.corpus.arabic.utils.pyarabic import araby

__algorithm__ = ["Dr. Shereen Khoja (خوجة شرين)"]
__authors__ = []
__license__ = ""
__version__ = "Beta"

class KhojaStemmer:

    def stem(self, token):
        stemmed = token
        return stemmed
