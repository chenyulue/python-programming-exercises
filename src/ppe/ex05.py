"""Write a fizz-buzz word game."""

def get_fizz_buzz(num: int) -> str:
    if num % 15 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)

def fizz_buzz(up: int) -> None:
    s =  []
    for num in range(1, up+1):
        s.append(get_fizz_buzz(num))

    print(*s)