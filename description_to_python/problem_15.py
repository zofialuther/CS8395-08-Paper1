

def maxProduct(nums):
    max = nums[0]
    min = nums[0]
    result = nums[0]
    
    for i in range (1, len(nums)):
        max_temp = max
        min_temp = min
        
        max = max(max_temp * nums[i], min_temp * nums[i], nums[i])
        min = min(max_temp * nums[i], min_temp * nums[i], nums[i])
        result = max(result, max)
    
    return result