def is_valid(s):
    stack = []
    for char in s:
        if char in ["(", "{", "["]:
            stack.append(char)
        elif char == ")":
            if not stack or stack.pop() != "(":
                return False
        elif char == "}":
            if not stack or stack.pop() != "{":
                return False
        elif char == "]":
            if not stack or stack.pop() != "[":
                return False
    return not stack