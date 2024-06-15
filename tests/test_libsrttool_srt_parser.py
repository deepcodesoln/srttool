import unittest

from libsrttool import srt_parser
from tests.simple_srt_file import SIMPLE_SRT_CONTENT


class TestLibSRTToolSRTParser(unittest.TestCase):
    def test_parse_srt(self):
        es = list(srt_parser.parse_srt(SIMPLE_SRT_CONTENT))
        # TODO(orphen) test timestamp when parsed
        self.assertTrue(es[0].num == 1)
        self.assertTrue(es[0].text == "foo bar baz\n")

        self.assertTrue(es[1].num == 2)
        self.assertTrue(es[1].text == "baz bar\nfoo\n")
