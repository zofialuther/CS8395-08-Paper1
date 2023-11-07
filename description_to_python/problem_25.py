

def fizz_buzz(n):
  strings = []
  for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        strings.append('FizzBuzz')
    elif i % 3 == 0:
        strings.append('Fizz')
    elif i % 5 == 0:
        strings.append('Buzz')
    else:
        strings.append(str(i))
  return strings