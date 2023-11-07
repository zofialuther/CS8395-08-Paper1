

def check_valid_symbols(string):
    stack = []
    open_symbols = ["(", "{", "["]
    closing_symbols = [")", "}", "]"]
    for char in string:
        if char in open_symbols:
            stack.append(char)
        if char in closing_symbols:
            if len(stack) == 0 or stack.pop() != open_symbols[closing_symbols.index(char)]:
                return False
    return len(stack) == 0