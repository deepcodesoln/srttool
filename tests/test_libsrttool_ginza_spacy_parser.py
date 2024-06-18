"""Tests for the libsrttool.ginza_spacy_parser module."""

import json
import unittest

from libsrttool.ginza_spacy_parser import (
    Token,
    spacy_to_tokens,
    spacy_to_word_frequencies,
)
from tests.simple_ginza_spacy_json import SIMPLE_GINZA_SPACY_JSON


class TestLibSRTToolGinzaSpaCyParser(unittest.TestCase):
    def test_spacy_to_tokens(self):
        json_content = json.loads(SIMPLE_GINZA_SPACY_JSON)
        tokens = list(spacy_to_tokens(json_content))
        self.assertIn(Token(lemma="俺", norm="俺"), tokens)
        self.assertIn(Token(lemma="中国", norm="中国"), tokens)
        self.assertIn(Token(lemma="行く", norm="行く"), tokens)
        self.assertIn(Token(lemma="てめえ", norm="てまえ"), tokens)

    def test_spacy_to_word_frequencies(self):
        json_content = json.loads(SIMPLE_GINZA_SPACY_JSON)
        words = spacy_to_word_frequencies(json_content)

        self.assertEqual(4, len(words))
        for word, count in words:
            if word.lemma == "俺":
                self.assertEqual(2, count)
            elif word.lemma == "中国":
                self.assertEqual(1, count)
            elif word.lemma == "行く":
                self.assertEqual(1, count)
            elif word.lemma == "てめえ":
                self.assertEqual(1, count)
            else:
                self.assertTrue(False)
