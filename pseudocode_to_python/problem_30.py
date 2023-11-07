

def canJump(nums):
  lastGoodIndex = len(nums) - 1

  for i in range(len(nums) - 1, -1, -1):
    if i + nums[i] >= lastGoodIndex:
      lastGoodIndex = i

  if lastGoodIndex == 0:
    return True
  else:
    return False