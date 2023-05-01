"""Discovered the use of left shift operator (<<) 
   to calculate the number of grains on a square,
   instead of using the ** operator or pow() func."""

def square(number):
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")    
        
    return 1 << (number - 1)
        

def total():
    return (1 << 64) - 1
