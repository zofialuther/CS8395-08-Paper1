

def reverse(x):
  reversed = 0
  if x < 0 or x > 2**20 -1:
    return 0
  while not x == 0:
    reversed = reversed * 10 + x % 10
    x = x // 10
  if reversed < -2**31 or reversed > 2**31 - 1:
    return 0
  else:
    return int(reversed)