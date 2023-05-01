def is_armstrong_number(number: int) -> bool:
    string_num: str = str(number)
    total: int = sum(int(digit)**len(string_num) for digit in string_num)
    
    return total == number
