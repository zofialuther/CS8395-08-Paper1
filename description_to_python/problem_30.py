

def canReachTheLastIndex(array): 
  maxReachablePos = 0 
  for i in range(len(array)): 
    maxReachablePos = max(maxReachablePos, i + array[i])
    if maxReachablePos >= len(array) - 1:
      return True 
  return False