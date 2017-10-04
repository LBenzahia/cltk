"""Assem's Snowball Stemmer module for Classical Arabic"""

from cltk.corpus.arabic.alphabet import *
from cltk.corpus.arabic.utils.pyarabic import araby

__algorithm__ = ["Assem Chelli (شلي عاصم)", "Lakhdar Benzahia (بن زاهية لخضر)"]
__authors__ = ['Lakhdar Benzahia, <lakhdar.benzahia@gmail.com>, CLTK version ']
__license__ = "BSD_License see the link https://github.com/assem-ch/arabicstemmer/blob/master/BSD_License.txt"
__version__ = "Beta"

class AssemStemmer:


    def stem(self, token):
        """ take a word and return its stem/root"""
        stemmed = token
        return stemmed
