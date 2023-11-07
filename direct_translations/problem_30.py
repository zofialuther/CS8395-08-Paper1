

def canJump(nums):
  lastGoodIndex = len(nums) - 1
  for i in range(len(nums) - 1, -1, -1):
    if i + nums[i] >= lastGoodIndex:
      lastGoodIndex = i
  return lastGoodIndex == 0