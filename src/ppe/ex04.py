"""Write four functions to calulate the area, perimeter, volume, and surface
area."""


def raise_if_any_negative(*args: float | int):
    for num in args:
        if num < 0:
            raise ValueError(f"Only non-negative arguments are allowed: {num}")

def area(length: float | int, width: float | int) -> float | int:
    raise_if_any_negative(length, width)
    return length * width


def perimeter(length: float | int, width: float | int) -> float | int:
    raise_if_any_negative(length, width)
    return length * 2 + width * 2


def volume(length: float | int, width: float | int, height: float | int) -> float | int:
    raise_if_any_negative(length, width, height)
    return length * width * height


def surface_area(
    length: float | int, width: float | int, height: float | int
) -> float | int:
    raise_if_any_negative(length, width, height)
    return length * width * 2 + length * height * 2 + width * height * 2
