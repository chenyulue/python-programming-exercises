import pytest
from ppe import ex04

def test_area():
    assert ex04.area(10, 10) == 100
    assert ex04.area(0, 9999) == 0
    assert ex04.area(5, 8) == 40

def test_perimeter():
    assert ex04.perimeter(10, 10) == 40
    assert ex04.perimeter(0, 9999) == 19998
    assert ex04.perimeter(5, 8) == 26

def test_volume():
    assert ex04.volume(10, 10, 10) == 1000
    assert ex04.volume(9999, 0, 9999) == 0
    assert ex04.volume(5, 8, 10) == 400

def test_surface_area():
    assert ex04.surface_area(10, 10, 10) == 600
    assert ex04.surface_area(9999, 0, 9999) == 199960002
    assert ex04.surface_area(5, 8, 10) == 340

def test_function_with_negative_arguments():
    match_format = "Only non-negative arguments are allowed: {}"
    
    with pytest.raises(ValueError, match=match_format.format(-1)):
        ex04.area(-1, 10)

    with pytest.raises(ValueError, match=match_format.format(-5)):
        ex04.perimeter(10, -5)

    with pytest.raises(ValueError, match=match_format.format(-1)):
        ex04.volume(1, 2, -1)

    with pytest.raises(ValueError, match=match_format.format(-5)):
        ex04.surface_area(-5, -2, -3)