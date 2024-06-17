"""
Utilities to convert spaCy-like JSON objects to word frequency lists.
This module assumes JSON follows the ginza tool's spaCy-like JSON format
with an example shown here:
https://github.com/megagonlabs/ginza?tab=readme-ov-file#execute-ginza-command

Note the spaCy JSON schema is here:
https://spacy.io/api/data-formats#json-input
"""

import argparse
import json
from collections import defaultdict
from typing import DefaultDict, NamedTuple


def extend_cli(sp: argparse._SubParsersAction):
    """
    Extend a CLI with an interface for this module.

    Args:
        sp: The subparsers object on a CLI to extend. This function adds and
            configures one or more new subparsers.
    """
    parser = sp.add_parser(
        "word_frequency",
        help="produce word frequency lists from spaCy-like JSON content",
    )
    parser.add_argument(
        "json_file",
        help="pathname of the spaCy-like JSON content to process",
    )
    parser.add_argument(
        "output_file",
        help="the pathname to write the word frequency list to",
    )
    parser.set_defaults(func=main)


DESIRED_PARTS_OF_SPEECH = ["PROPN", "VERB", "PRON"]
WHITESPACE = "空白"


class Word(NamedTuple):
    """ """

    lemma: str
    norm: str

    def __hash__(self):
        return hash(self.lemma + self.norm)

    def __str__(self):
        return f"{self.norm} ({self.lemma})"


def word_frequency(json_content) -> list[tuple[Word, int]]:
    """ """
    words: DefaultDict[Word, int] = defaultdict(int)
    for block in json_content:
        for paragraph in block["paragraphs"]:
            for sentence in paragraph["sentences"]:
                for token in sentence["tokens"]:
                    if token["pos"] not in DESIRED_PARTS_OF_SPEECH:
                        continue
                    if token["tag"] == WHITESPACE:
                        continue
                    words[Word(token["lemma"], token["norm"])] += 1
    sorted_words = sorted(words.items(), key=lambda x: x[1], reverse=True)
    return sorted_words


def main(args: argparse.Namespace):
    with open(args.json_file, "r") as f:
        json_content = json.load(f)
    words = word_frequency(json_content)
    for word, count in words:
        print(f"{word}, {count}")
    # with open(args.output_file, "w") as f:
    #     for l in lines:
    #         # Write an extra newline per line to preserve SRT-like format.
    #         f.write(l + "\n")
