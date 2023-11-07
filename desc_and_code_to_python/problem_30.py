

def canJump(nums):
  lastGoodIndex = len(nums) - 1
  i = len(nums) - 1
  while i >= 0:
    if i + nums[i] >= lastGoodIndex:
      lastGoodIndex = i
    i -= 1
  return lastGoodIndex == 0