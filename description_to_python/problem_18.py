

def rotate(nums, k):
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    reverse(nums, 0, len(nums))

def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end-1] = nums[end-1], nums[start]
        start += 1
        end -= 1