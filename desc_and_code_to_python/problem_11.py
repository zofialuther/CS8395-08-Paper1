

def fib(N):
  if N <= 1:
    return N
  a, b = 0, 1
  while N > 1:
    sum = a + b
    a = b
    b = sum
    N -= 1
  return b