from ppe import ex08

def test_read_and_write(tmp_path):
    file = tmp_path / "greet.txt"
    ex08.write_to_file(file, "Hello!\n")
    ex08.append_to_file(file, "Goodbye!\n")
    assert ex08.read_from_file(file) == "Hello!\nGoodbye!\n"