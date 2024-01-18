from io import StringIO
from ppe import ex01

def test_greet(monkeypatch, capsys):
    with capsys.disabled():
        monkeypatch.setattr("sys.stdin", StringIO("Alice"))

    ex01.greet()
    out, _ = capsys.readouterr()
    expected = "Hello, world!\nWhat is your name?\nHello, Alice\n"
    assert out == expected