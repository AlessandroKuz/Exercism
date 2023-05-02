def is_valid(function):
    def inner(sides: list[int]):
        return sum(sides) > 2 * max(sides) and function(sides)
    return inner

@is_valid
def equilateral(sides: list[int]) -> bool:
    return len(set(sides)) == 1
    
@is_valid
def isosceles(sides: list[int]) -> bool:
    return len(set(sides)) < 3


@is_valid
def scalene(sides: list[int]) -> bool:
    return len(set(sides)) == 3
