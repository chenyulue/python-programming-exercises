"""Basic file input/output"""

def write_to_file(filename: str, text: str) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

def append_to_file(filename: str, text: str) -> None:
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)

def read_from_file(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
    return text