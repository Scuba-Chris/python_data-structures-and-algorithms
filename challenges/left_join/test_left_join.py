import pytest
from challenges.left_join.left_join import left_join

def test_left_join():
    d1 = {
    'wrath':'anger',
    'outfit': 'garb',
    'guide':'usher',
    }
    d2 = {
    'wrath' : 'delight',
    'flow' : 'jam',
    'guide' : 'follow',
    }

    actual = left_join(d1,d2)
    expected = [['wrath', 'anger', 'delight'], 
    ['outfit', 'garb', None], ['guide', 'usher', 'follow']]

    assert actual == expected