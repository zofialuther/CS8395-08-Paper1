

def gcd(numbers):
    """
    Calculate the greatest common divisor for a given int array of numbers.
    """
    a = numbers[0]
    b = numbers[1]
    
    while b != 0:
        temp = b
        b = a % b
        a = temp
    
    return a