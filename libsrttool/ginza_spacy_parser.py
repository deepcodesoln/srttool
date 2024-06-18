"""
Parsing utilities for the Ginza tool's spaCy-like output.

Ginza: https://github.com/megagonlabs/ginza
"""

from collections import defaultdict
from typing import DefaultDict, Iterable, NamedTuple

DESIRED_PARTS_OF_SPEECH = ["PROPN", "VERB", "PRON"]
"""The spaCy-like content ``pos`` value for desired parts of speech."""

WHITESPACE = "空白"
"""The spaCy-like content ``tag`` value for whitespace tokens."""


class Token(NamedTuple):
    """A token in spaCy-like content."""

    lemma: str
    """The lemma form of the token."""

    norm: str
    """The normative form of the token."""

    def __eq__(self, other: object):
        if isinstance(other, Token):
            return self.lemma == other.lemma and self.norm == other.norm
        else:
            return False

    def __hash__(self):
        return hash(self.lemma + self.norm)

    def __str__(self):
        return f"{self.norm} ({self.lemma})"


def spacy_to_tokens(json_content: dict) -> Iterable[Token]:
    """
    Parse individual tokens out of spaCy-like JSON content. Ignore tokens that
    are not in :data:`DESIRED_PARTS_OF_SPEECH` or that have the ``tag``
    :data:`WHITESPACE`.

    Args:
        json_content: the spaCy-like JSON content to parse tokens out of.
    Returns:
        Individual tokens parsed out of the ``json_content``.
    """
    for block in json_content:
        for paragraph in block["paragraphs"]:
            for sentence in paragraph["sentences"]:
                for token in sentence["tokens"]:
                    if token["pos"] not in DESIRED_PARTS_OF_SPEECH:
                        continue
                    if token["tag"] == WHITESPACE:
                        continue
                    yield Token(token["lemma"], token["norm"])


def spacy_to_word_frequencies(json_content: dict) -> list[tuple[Token, int]]:
    """
    Convert spaCy-like JSON content into a list of words and their frequencies
    from the JSON corpus.

    Args:
        json_content: the spaCy-like JSON content to analyze.
    Returns:
        A list of pairs of :class:`Token` s (words) and how many times each
        token appeared in the corpus.
    """
    words: DefaultDict[Token, int] = defaultdict(int)
    for t in spacy_to_tokens(json_content):
        words[t] += 1
    sorted_words = sorted(words.items(), key=lambda x: x[1], reverse=True)
    return sorted_words
