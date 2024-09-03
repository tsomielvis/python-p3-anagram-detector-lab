#!/usr/bin/env python3

import pytest
from anagram import Anagram

@pytest.fixture
def listen():
    return Anagram("listen")

@pytest.mark.parametrize("word_list, expected", [
    (['enlists', 'google', 'inlets', 'banana'], ['inlets']),
    (['enlist', 'google', 'silent', 'tinsel'], ['silent', 'tinsel']),
    (['enlists', 'google', 'banana'], []),
    (['enlist', 'google', 'silent'], ['silent']),
    ([], []),
    (['cat', 'dog', 'bird'], []),
    (['enlist', 'tinsel', 'silent', 'inlets'], ['enlist', 'tinsel', 'silent', 'inlets']),
])
def test_anagram(listen, word_list, expected):
    assert listen.match(word_list) == expected
