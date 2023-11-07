

def Fibonacci(N): 
    if N<0: 
        return 0
    # First Fibonacci number is 0 
    elif N==1: 
        return 0
    # Second Fibonacci number is 1 
    elif N==2: 
        return 1
    else: 
        return Fibonacci(N-1)+Fibonacci(N-2) 

# Test
Fibonacci(5)