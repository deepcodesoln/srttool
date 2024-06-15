"""
Utilities to convert an SRT file to subtitle text without metadata.
"""

from libsrttool import srt_parser


def to_dialog(srt: list[str]) -> list[str]:
    """
    Convert SRT content to a subtitle text without metadata.

    Args:
       srt: A list of lines from an SRT file. The SRT file is expected to
           follow the schema assumed by ``srttool`` .
    Returns: A list of subtitle text less metadata. Blocks of text in the SRT
        content containing newlines are combined into a single string, but the
        newline characters are preserved.
    """
    text: list[str] = []
    for e in srt_parser.parse_srt(srt):
        text.append(e.text)
    return text
