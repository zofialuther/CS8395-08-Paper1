

def customSort(strs):
  strs.sort(key=lambda x: (int(x), x) if x.isdigit() else x)
  return strs