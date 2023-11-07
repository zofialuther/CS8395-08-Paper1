def customSort(strs):
  strs.sort(key = lambda a, b: int(a) - int(b) if int(a) == int(b) else a.compareTo(b))
  return strs


print(customSort(["5"]))
