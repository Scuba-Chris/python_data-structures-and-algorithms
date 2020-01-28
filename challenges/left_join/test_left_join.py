import pytest
from challenges.left_join.left_join import left_join

def test_left_join_one():
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

def test_left_join_two():
    d1 = {
        'small' : 'tiny',
        'big' : 'giant',
        'wet' : 'moist'
    }

    d2 = {
        'green' : 'blue',
        'small' : 'huge',
        'moist' : 'dry'
    }

    actual = left_join(d1, d2)
    expected = [['small', 'tiny', 'huge'], ['big', 'giant', None], 
    ['wet', 'moist', None]]

    assert actual == expected

def test_left_join_three():
    d1 = {
        'small' : 'tiny',
        'big' : 'giant',
        'wet' : 'moist'
    }
    d2 = {
        'wrath' : 'delight',
        'flow' : 'jam',
        'guide' : 'follow',
    }

    actual = left_join(d1, d2)
    epxpected = [['small', 'tiny', None], ['big', 'giant', None],
    ['wet', 'moist', None]]

    assert actual == epxpected