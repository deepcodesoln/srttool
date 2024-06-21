"""
Utilities to convert an SRT file to subtitle text without metadata.
"""

import argparse
import glob
import os
import re
import sys

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
        help="convert one or more SRT files to a text file containing only subtitle text",
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--srt_file",
        help="pathname of SRT file to process",
    )
    group.add_argument(
        "--srt_dir",
        help="pathname of a directory containing SRT files to process",
    )
    parser.add_argument(
        "output_pathname",
        help="the pathname to write the dialog file(s) to; "
        + "if processing a single file, must be a filename; "
        + "if processing a directory of files, must be a directory",
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


def main(args: argparse.Namespace) -> int:
    if args.srt_file:
        if not os.path.isfile(args.srt_file):
            print(f"{args.srt_file} must be an ordinary file", file=sys.stderr)
            return 1

        with open(args.srt_file, "r") as f:
            lines = f.readlines()
        lines = to_dialog(lines)
        with open(args.output_pathname, "w") as f:
            for l in lines:
                f.write(l)
    else:  # args.srt_dir
        if not os.path.isdir(args.srt_dir):
            print(f"{args.srt_dir} must be a directory", file=sys.stderr)
            return 1
        if not os.path.exists(args.output_pathname):
            os.makedirs(args.output_pathname, exist_ok=True)

        files = glob.glob(os.path.join(args.srt_dir, "*.srt"))
        for srt_file in files:
            with open(srt_file, "r") as f:
                lines = f.readlines()
            lines = to_dialog(lines)

            output_file_base = os.path.basename(srt_file)
            output_file = os.path.splitext(output_file_base)[0] + ".txt"
            output_pathname = os.path.join(args.output_pathname, output_file)
            with open(output_pathname, "w") as f:
                for l in lines:
                    f.write(l)

    return 0
