def leap_year(year: int) -> bool:
    """Return a bool value of whether the given year
    is a leap one or not."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)