

def maxProduct(nums):
  if nums is None or len(nums) == 0:
    return 0
  max_val = nums[0]
  min_val = nums[0]
  result = nums[0]
  for i in range(1, len(nums)):
    temp = max_val
    max_val = max(max(max_val * nums[i], min_val * nums[i]), nums[i])
    min_val = min(min(temp * nums[i], min_val * nums[i]), nums[i])
    if max_val > result:
      result = max_val
  return result