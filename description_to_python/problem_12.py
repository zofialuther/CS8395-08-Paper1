

def singleNumber(nums):
    result = 0
    for num in nums:
        result = result ^ num
    return result