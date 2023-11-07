

def myAtoi(s):
  if not s or s == '':
    return 0

  s = s.strip()
  sign = 1
  index = 0
  total = 0
 
  if s[0] == '+' or s[0] == '-':
    sign = 1 if s[0] == '+' else -1
    index += 1

  while index < len(s):
    digit = ord(s[index]) - ord('0')

    if digit < 0 or digit > 9:
      break
    
    if total > (2**31 - 1) // 10 or (total == (2**31 - 1) // 10 and digit > (2**31 - 1) % 10):
      return 2**31 - 1 if sign == 1 else -2**31

    total = 10 * total + digit
    index += 1

  return total * sign