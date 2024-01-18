"""Given an integer parameter named `number`, write a function `ordinal_suffix` to
convert it to an ordinal numeral.
"""

def ordinal_suffix(number: int) -> str:
    match (number % 100, number % 10):
        case (11, _) | (12, _) | (13, _):
            return f"{number}th"
        case (_, 1):
            return f"{number}st"
        case (_, 2):
            return f"{number}nd"
        case (_, 3):
            return f"{number}rd"
        case _:
            return f"{number}th"