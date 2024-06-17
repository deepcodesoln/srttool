"""
Utilities to convert an SRT file to subtitle text without metadata.
"""

import argparse
import re

from libsrttool import srt_parser


def extend_cli(sp: argparse._SubParsersAction):
    """
    Extend a CLI with an interface for this module.

    Args:
        sp: The subparsers object on a CLI to extend. This function adds and
            configures one or more new subparsers.
    """
    parser = sp.add_parser(
        "to_dialog",
        help="convert an SRT file to a text file containing only subtitle text",
    )
    parser.add_argument("srt_file", help="pathname of SRT file to process")
    parser.add_argument(
        "output_file",
        help="the pathname to write the dialog file to",
    )
    parser.set_defaults(func=main)


def to_dialog(srt: list[str]) -> list[str]:
    """
    Convert SRT content to a subtitle text without metadata. Special SRT
    formatting such as subtitle position is removed from text.

    Args:
       srt: A list of lines from an SRT file. The SRT file is expected to
           follow the schema assumed by ``srttool`` .
    Returns:
        A list of subtitle text less metadata. Blocks of text in the SRT
        content containing newlines are combined into a single string, but the
        newline characters are preserved.
    """
    subtitle_position = re.compile("{\\\\an.}")
    text: list[str] = []
    for e in srt_parser.parse_srt(srt):
        cleaned_text = re.sub(subtitle_position, "", e.text)
        text.append(cleaned_text)
    return text


def main(args: argparse.Namespace):
    with open(args.srt_file, "r") as f:
        lines = f.readlines()
    lines = to_dialog(lines)
    with open(args.output_file, "w") as f:
        for l in lines:
            f.write(l)
        f.close()
