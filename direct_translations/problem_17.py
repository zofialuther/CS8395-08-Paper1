

def findLHS(nums): 
  map = {}
  result = 0
  for num in nums: 
    map[num] = map.get(num, 0) + 1
  for key in map.keys(): 
    if key + 1 in map.keys(): 
      result = max(result, map[key] + map[key + 1])
  return result