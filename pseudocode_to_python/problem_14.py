

def sameCharCount(s):
    charCounts = {}
    count = -1

    for c in s:
        charCounts[c] = charCounts.get(c, 0) + 1

    for c in charCounts.values():
        if count == -1:
            count = c
        elif count != c:
            return False
    
    return True