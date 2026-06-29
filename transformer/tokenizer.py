"""
tokenizer.py

A simple word-level tokenizer implemented from scratch.
"""

from collections import Counter


class Tokenizer:
    """
    Converts text into integer token IDs and back again.
    """

    def __init__(self):
        self.word_to_index = {}
        self.index_to_word = {}
        self.vocabulary_size = 0