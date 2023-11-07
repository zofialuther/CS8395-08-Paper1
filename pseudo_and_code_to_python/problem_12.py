

def singleNumber(nums):
    single = 0
    for num in nums:
        single ^= num
    return single