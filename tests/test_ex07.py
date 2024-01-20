from ppe import ex07


def test_print_ascii_table(capsys):
    ex07.print_ascii_table()

    out = capsys.readouterr().out.rstrip()

    for line in out.split("\n"):
        codepoint, char = line[:-2], line[-1]
        assert int(codepoint) == ord(char)
