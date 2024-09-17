from src.math_operations import add, sub


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 5
    assert add(-2, 5) == 3
    assert add(6, 0) == 6
    assert add(1000000000, 1000000000) == 2000000000


def test_sub():
    assert sub(5, 3) == 2
    assert sub(1, -1) == 3
    assert sub(-2, 5) == -7
    assert sub(6, 0) == 6
    assert sub(1000000000, 1000000000) == 0