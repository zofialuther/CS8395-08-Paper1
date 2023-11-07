


def first_unique_char(string):
    freq = [0] * 26
    for c in string:
        freq[ord(c) - ord('a')] += 1
    
    for i in range(len(string)):
        if freq[ord(string[i]) - ord('a')] == 1:
            return i
    return -1