

def find_duplicates(nums):
    duplicates = []
    for num in nums:
        index = abs(num) - 1
        if nums[index] < 0:
            duplicates.append(abs(num))
        nums[index] = -nums[index]
    return duplicates