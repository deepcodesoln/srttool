"""
A tool to parse SRT subtitle files (primarily Japanese ones) and convert them
into formats for language study.

This tool assumes SRT files have the schema:

```
line_no (positive integer; ex: 1)
timestamp (hh:mm:ss,ms -> hh:mm:ss,ms; ex: 00:00:00,001 -> 00:00:01,100)
text (string, no enclosing quotes; ex: nani nani nani)
<empty line>
```
"""

import argparse

from libsrttool import srt_parser
from libsrttool.actions import to_dialog


def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("srt", help="pathname of SRT file to process")
    parser.add_argument(
        "--to-dialog",
        metavar="output_file",
        help="convert an SRT file to a text file containing only subtitle text; argument is output filename",
    )
    return parser.parse_args()


def main():
    args = cli()

    if args.to_dialog:
        with open(args.srt, "r") as f:
            lines = f.readlines()
        lines = to_dialog.to_dialog(lines)
        with open(args.to_dialog, "w") as f:
            for l in lines:
                # Write an extra newline per line to preserve SRT-like format.
                f.write(l + "\n")
            f.close()


if __name__ == "__main__":
    main()
