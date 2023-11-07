

def customSort(strs):
  numA = int(strs[0])
  numB = int(strs[1])
  if numA == numB:
    return strs[0] == strs[1]
  else:
    return numA - numB
  strs.sort()
  return strs