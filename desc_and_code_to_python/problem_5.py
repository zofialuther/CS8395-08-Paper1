

def customSort(strs):
    strs.sort(key=lambda x: (int(x), x))
    return strs