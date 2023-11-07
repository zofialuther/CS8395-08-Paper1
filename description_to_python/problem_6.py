

def gcd(arr): 
    a = arr[0]
    b = arr[1]
    while b != 0:
        b, a = a % b, b
    return a