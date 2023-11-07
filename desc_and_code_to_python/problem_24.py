

def firstUniqChar(s):
    frequency = [0] * 26
    for i in range(len(s)):
        frequency[ord(s[i]) - ord('a')] += 1
    for i in range(len(s)):
        if frequency[ord(s[i]) - ord('a')] == 1:
            return i
    return -1