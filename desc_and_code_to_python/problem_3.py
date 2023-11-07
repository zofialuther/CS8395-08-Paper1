

def isBalanced(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0 or stack.pop() != '(':
                return False
    return len(stack) == 0