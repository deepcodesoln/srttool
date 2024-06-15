"""
Parsing utilities for SRT files.
"""

from typing import Iterable, NamedTuple


class Timestamp(NamedTuple):
    """
    An SRT timestamp, where the timestamp is formatted as ``hr:mn:sc,ms`` .
    """

    hr: int
    mn: int
    sc: int
    ms: int

    def __str__(self):
        return f"{self.hr}:{self.mn}:{self:sc},{self.ms}"


class SRTElement(NamedTuple):
    """
    An SRT file element, meaning a block of text with corresponding subtitle
    number and timestamps.
    """

    num: int
    timestamp_from: Timestamp
    timestamp_to: Timestamp
    text: str

    def __str__(self):
        return (
            f"{self.num}\n"
            f"{self.timestamp_from} --> {self.timestamp_to}\n"
            f"{self.text}"
        )


def parse_srt(srt: list[str]) -> Iterable[SRTElement]:
    """
    Parse SRT content into individual elements.

    Args:
        srt: lines from an SRT file; the schema of the SRT file is assumed to
            match ``srttool`` 's expectations.
    Returns: An iterator over :class:`SRTElement` s parsed out of ``srt``.
    """
    i = iter(srt)
    try:
        while True:
            # orphen: I found some SRT files in the wild that begin with
            # the zero-width no-break space '\ufeff'; parse that off.
            num = int(next(i).lstrip("\ufeff").strip())
            timestamp = next(i).strip()
            text = ""
            while (text_e := next(i)) != "\n":
                text += text_e
            yield SRTElement(num, Timestamp(0, 0, 0, 0), Timestamp(0, 0, 0, 0), text)
    except StopIteration:
        pass
