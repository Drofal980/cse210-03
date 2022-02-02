from random import random

class Word_bank:

    def __init__(self):
        self._choosen_word = ''
        self._words = ['waffles','dogs','cats','class','happy']

    def choose_word(self):
        self._choosen_word = random(self._words)
    
    def get_word(self):
        return self._choosen_word
