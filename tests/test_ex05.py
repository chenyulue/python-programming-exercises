from ppe import ex05

def test_get_fizz_buzz():
    assert ex05.get_fizz_buzz(30) == "FizzBuzz"
    assert ex05.get_fizz_buzz(6) == "Fizz"
    assert ex05.get_fizz_buzz(25) == "Buzz"

def test_fizz_buzz(capsys):
    ex05.fizz_buzz(35)

    expected = (
        "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz "
        "16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz "
        "31 32 Fizz 34 Buzz"
    )
    out = capsys.readouterr().out.rstrip()
    assert out == expected