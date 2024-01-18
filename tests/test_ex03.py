from ppe import ex03

def test_is_odd():
    assert ex03.is_odd(42) is False
    assert ex03.is_odd(9999) is True
    assert ex03.is_odd(-10) is False
    assert ex03.is_odd(3.1415) is False

def test_is_even():
    assert ex03.is_even(42) is True
    assert ex03.is_even(9999) is False
    assert ex03.is_even(-10) is True
    assert ex03.is_even(-11) is False
    assert ex03.is_even(3.1415) is False
    