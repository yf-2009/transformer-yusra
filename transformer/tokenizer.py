"""
tokenizer.py

Implements a simple word-level tokenizer from scratch.
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

    def build_vocabulary(self, texts):
        """
        Builds a vocabulary from a list of sentences.
        """

        word_counts = Counter()

        for sentence in texts:
            words = sentence.lower().split()
            word_counts.update(words)

        # Reserve token ID 0 for unknown words
        self.word_to_index = {
            "<UNK>": 0
        }

        for index, word in enumerate(word_counts.keys(), start=1):
            self.word_to_index[word] = index

        self.index_to_word = {
            index: word
            for word, index in self.word_to_index.items()
        }

        self.vocabulary_size = len(self.word_to_index)

    def encode(self, text):
        """
        Converts a string into a list of token IDs.
        """

        words = text.lower().split()

        return [
            self.word_to_index.get(word, self.word_to_index["<UNK>"])
            for word in words
        ]

    def decode(self, token_ids):
        """
        Converts token IDs back into a string.
        """

        words = [
            self.index_to_word[token]
            for token in token_ids
        ]

        return " ".join(words)