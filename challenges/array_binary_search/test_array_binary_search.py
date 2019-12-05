from array_binary_search import binary_search

def test_binary_search_one():
    expected = 1
    actual = binary_search([8, 5 , 52, 15, 150, 81],8)
    assert actual == expected

def test_binary_search_neg_one():
    expected = -1
    actual = binary_search([8, 5 , 52, 15, 150, 81], 9)
    assert actual == expected