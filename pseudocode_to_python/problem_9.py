

def parentheses_checker(s):
    stack = [] 
    for char in s: 
        if char == "(": 
            stack.append(char) 
        else: 
            if len(stack) == 0: 
                return False 
            if char == ")" and stack[-1] != "(": 
                return False 
            stack.pop() 
    return len(stack) == 0