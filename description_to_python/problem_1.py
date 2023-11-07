

def is_palindrome(string):
    string = string.lower().replace(' ', '')
    start = 0
    end = len(string) - 1
    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True