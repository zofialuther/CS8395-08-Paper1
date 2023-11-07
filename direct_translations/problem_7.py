

def maxSubArraySum(nums): 
  if len(nums) == 0: 
    return 0
  maxSoFar = nums[0]
  currentMax = nums[0]
  for i in range(1, len(nums)): 
    currentMax = max(nums[i], currentMax + nums[i])
    maxSoFar = max(maxSoFar, currentMax)
  return maxSoFar