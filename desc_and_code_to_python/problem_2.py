

def hasUniqueChars(s):
    charSet = set()
    for c in s:
        if c in charSet:
            return False
        charSet.add(c)
    return True