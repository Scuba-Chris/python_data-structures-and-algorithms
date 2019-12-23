from stacks_and_queues import Node, Stack, Queue
import pytest

def test_push(values):
    st = Stack()
    values = [1,2,3,4]
    for num in values:
        st.push(num)

    expected = 4
    actual = st.peek()
    assert expected == actual

def test_peek():
    st = Stack()
    values = [1,2,3,4]
    for num in values:
        st.push(num)

    expected = 4
    actual = st.peek()
    assert expected == actual