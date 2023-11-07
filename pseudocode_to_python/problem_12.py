

def single_num(nums):
  single = 0
  for num in nums:
    single = single ^ num
  return single