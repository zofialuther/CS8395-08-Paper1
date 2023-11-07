

def maxSubArraySum(nums):
  # check if the length of nums is 0
  if len(nums) == 0:
    # return 0
    return 0
  
  # declare a variable maxSoFar and set it to the first element in nums 
  maxSoFar = nums[0]
  # declare a variable currentMax and set it to the first element in nums
  currentMax = nums[0] 
  # loop through the elements of nums
  for i in range(1, len(nums)):
    # set currentMax to the max of the current element and the sum of the current element and the currentMax
    currentMax = max(nums[i], currentMax + nums[i])
    # set maxSoFar to the max of maxSoFar and currentMax
    maxSoFar = max(maxSoFar, currentMax)
  # return maxSoFar
  return maxSoFar