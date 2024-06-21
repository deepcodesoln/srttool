"""
Utilities to convert spaCy-like JSON objects to word frequency lists.
This module assumes JSON follows the ginza tool's spaCy-like JSON format
with an example shown here:
https://github.com/megagonlabs/ginza?tab=readme-ov-file#execute-ginza-command

Note the spaCy JSON schema is here:
https://spacy.io/api/data-formats#json-input
"""

import argparse
import glob
import json
import os

from libsrttool import ginza_spacy_parser


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
        "json_files",
        help="pathname of the spaCy-like JSON content to process; "
        + "if a directory, process all JSON files in the directory; "
        + "if a single file, process just that file",
    )
    parser.add_argument(
        "output_file",
        help="the pathname to write the word frequency list to; "
        + "each line has the form `lemma (norm), count`",
    )
    parser.set_defaults(func=main)


def main(args: argparse.Namespace) -> int:
    json_files = []
    if os.path.isfile(args.json_files):
        json_files = [args.json_files]
    else:  # os.path.isdir
        json_files = glob.glob(os.path.join(args.json_files, "*.json"))

    json_content = []
    for json_file in json_files:
        with open(json_file, "r") as f:
            json_content.extend(json.load(f))
    words = ginza_spacy_parser.spacy_to_word_frequencies(json_content)
    with open(args.output_file, "w") as f:
        for word, count in words:
            f.write(f"{word}, {count}\n")

    return 0
