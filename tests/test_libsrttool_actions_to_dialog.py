import unittest

from libsrttool.actions import to_dialog
from tests.simple_srt_file import SIMPLE_SRT_CONTENT


class TestLibSRTToolActionsToDialog(unittest.TestCase):
    def test_to_dialog(self):
        text = to_dialog.to_dialog(SIMPLE_SRT_CONTENT)
        self.assertTrue(text[0] == "foo bar baz\n")
        self.assertTrue(text[1] == "baz bar\nfoo\n")
