from challenges.repeated_word.repeated_word import repeated_word
import pytest

def test_repeated_word_one():
    string = "Once upon a time, there was a brave princess who..."
    expected = 'a'
    actual = repeated_word(string)
    
    assert expected == actual

def test_repeated_word_two():
    string = 'It was a queer, sultry summer, the summer they electrocuted the Rosenbergs'
    expected = 'summer'
    actual = repeated_word(string)

    assert expected == actual
    
def test_repeated_word_three():
    string = "can't and won't"
    expected = None
    actual = repeated_word(string)

    assert expected == actual