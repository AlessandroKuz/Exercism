def steps(number: int) -> int:
    """The Collatz Conjecture implementation:
    given a number return the number of steps
    necessary to reduce it to 1.
    """
    steps: int = 0
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    while number != 1:
        number = (number / 2) if (number % 2 == 0) else (number * 3) + 1
        steps += 1
    return steps
