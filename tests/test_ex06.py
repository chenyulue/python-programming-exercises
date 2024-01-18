from ppe import ex06


def test_ordinal_suffix():
    assert ex06.ordinal_suffix(0) == "0th"
    assert ex06.ordinal_suffix(1) == "1st"
    assert ex06.ordinal_suffix(2) == "2nd"
    assert ex06.ordinal_suffix(3) == "3rd"
    assert ex06.ordinal_suffix(4) == "4th"
    assert ex06.ordinal_suffix(10) == "10th"
    assert ex06.ordinal_suffix(11) == "11th"
    assert ex06.ordinal_suffix(12) == "12th"
    assert ex06.ordinal_suffix(13) == "13th"
    assert ex06.ordinal_suffix(14) == "14th"
    assert ex06.ordinal_suffix(101) == "101st"
    assert ex06.ordinal_suffix(111) == "111th"
    assert ex06.ordinal_suffix(212) == "212th"
    assert ex06.ordinal_suffix(121) == "121st"
