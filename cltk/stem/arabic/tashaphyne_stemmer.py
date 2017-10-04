"""Tashaphyne Stemmer module for Classical Arabic"""

from cltk.corpus.arabic.alphabet import *
from cltk.corpus.arabic.utils.pyarabic import araby

__algorithm__ = ["Dr. Taha Zerrouki (زروقي طه )"]
__authors__ = ['Lakhdar Benzahia, <lakhdar.benzahia@gmail.com>, CLTK version', 'Dr. Taha Zerrouki, <taha_zerrouki at gmail dot com>, Original author ']
__license__ = " GNU General Public License v3.0 see the link https://github.com/linuxscout/tashaphyne/blob/master/LICENSE"
__version__ = "Beta for CLTK"
__copyright__ = 'Arabtechies,  Arabeyes,   Taha Zerrouki'

class TashaphyneStemmer:

    def stem(self, token):
        stemmed = token
        return stemmed
