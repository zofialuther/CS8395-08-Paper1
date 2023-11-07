

def findMaxConsecutiveOnes(nums):
    maxConsecutive = 0
    currentConsecutive = 0
    for num in nums:
        if num == 1:
            currentConsecutive += 1
            maxConsecutive = max(maxConsecutive, currentConsecutive)
        else:
            currentConsecutive = 0
    return maxConsecutive