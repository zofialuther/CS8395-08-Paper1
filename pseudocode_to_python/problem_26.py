

def isValid(s):
  stack = []
  for c in s:
    if c == '(' or c == '{' or c == '[':
      stack.append(c)
    elif c == ')' and stack and stack[-1] == '(':
      stack.pop()
    elif c == '}' and stack and stack[-1] == '{':
      stack.pop()
    elif c == ']' and stack and stack[-1] == '[':
      stack.pop()
    else:
      return False
  return not stack