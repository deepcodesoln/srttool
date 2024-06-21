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
import sys

from libsrttool import srt_parser
from libsrttool.actions import to_dialog, word_frequency


def cli() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    subparsers = parser.add_subparsers(help="actions")
    to_dialog.extend_cli(subparsers)
    word_frequency.extend_cli(subparsers)
    return parser.parse_args()


def main():
    args = cli()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
