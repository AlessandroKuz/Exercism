def square_of_sum(number: int) -> int:
    """Returns the square of the sum of numbers
    up until the given number as a parameter."""
    return (number*(number+1)//2)**2


def sum_of_squares(number: int) -> int:
    """Returns the sum of the square of numbers
    up until the given number as a parameter."""
    return number*(number+1)*(2*number+1)//6


def difference_of_squares(number: int) -> int:
    """Returns the difference between a sum of
    squares and the square of a sum."""
    return square_of_sum(number) - sum_of_squares(number)