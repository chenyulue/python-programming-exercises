from ppe import ex02


def test_convert_to_celsius():
    assert ex02.convert_to_celsius(0) == -17.77777777777778
    assert ex02.convert_to_celsius(180) == 82.22222222222223


def test_convert_to_fahrenheit():
    assert ex02.convert_to_fahrenheit(0) == 32
    assert ex02.convert_to_fahrenheit(100) == 212


def test_convert_identiry():
    assert ex02.convert_to_celsius(ex02.convert_to_fahrenheit(15)) == 15
    assert ex02.convert_to_celsius(ex02.convert_to_fahrenheit(42)) == 42
