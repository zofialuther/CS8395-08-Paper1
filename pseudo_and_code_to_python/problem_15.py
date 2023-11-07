

def maxProduct(nums):
  if nums is None or len(nums) == 0:
    return 0
  
  max_prod = nums[0]
  min_prod = nums[0]
  result = nums[0]
  
  for i in range(1, len(nums)):
    temp = max_prod
    max_prod = max(max(max_prod * nums[i], min_prod * nums[i]), nums[i])
    min_prod = min(min(temp * nums[i], min_prod * nums[i]), nums[i])
    if max_prod > result:
      result = max_prod
  
  return result