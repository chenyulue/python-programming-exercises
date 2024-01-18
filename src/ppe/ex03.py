"""Write two functions, `is_odd` and `is_even`, with a single numeric parameter
named `number` to determine whether the `nubmer` is odd or even.
"""


def is_odd(number: int | float) -> bool:
    return number % 2 == 1

def is_even(number: int | float) -> bool:
    return number % 2 == 0