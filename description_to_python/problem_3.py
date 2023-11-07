

def parentheses_balance(string):
  stack = []
  for char in string:
    if char == '(' or char == '[':
      stack.append(char)
    elif char == ')' or char == ']':
      if len(stack) == 0:
        return False
      top = stack.pop()
      if top == '(' and char != ')':
        return False
      if top == '[' and char != ']':
        return False
  return len(stack) == 0