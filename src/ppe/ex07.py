"""Write a `print_ascii_table` function to display the ASCII number and its
corresponding text characters, from 32 to 126. Characters in this range are
called *printable ASCII characters*"""

def print_ascii_table():
    for codepoint in range(32, 127):
        print(codepoint, chr(codepoint))

if __name__ == '__main__':
    print_ascii_table()