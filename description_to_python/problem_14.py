

def is_equal_char_count(s):
    initial_count = s.count(s[0])
    for char in s:
        if s.count(char) != initial_count:
            return False
    return True