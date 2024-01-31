"""Reimplement a `replace` string method"""

def find_and_replace(text: str, old_text: str, new_text: str):
    old_len = len(old_text)
    replaced_text = []
    i = 0
    while i <= len(text) - old_len:
        if text[i:i+old_len] == old_text:
            replaced_text.append(new_text)
            i += old_len
        else:
            replaced_text.append(text[i])
            i += 1
    replaced_text.append(text[i:])

    return ''.join(replaced_text)