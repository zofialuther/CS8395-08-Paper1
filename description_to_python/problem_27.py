

def convert_string_to_int(s):
    if not s or not s.strip(): 
        return 0
    s = s.strip()
    sign = -1 if s[0] == '-' else 1
    index = 0
    total = 0
    while index < len(s):
        if s[index].isdigit():
            total = (total * 10) + int(s[index])
            index += 1
        else:
            break
    return total * sign