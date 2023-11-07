

def find_duplicates(nums):
  '''
  Finds duplicate elements in an array of integers.

  Parameters:
  nums (list): List of integers

  Returns: 
  duplicates (list): List of duplicate integers 
  '''
  duplicates = []
  
  # Iterate through nums array 
  for num in nums:
    # Get the index of the element in the array 
    index = abs(num) - 1
    
    # If the element at that index is negative, add it to the duplicates list
    if nums[index] < 0 :
      duplicates.append(abs(num))
    
    # Set the element at index to negative 
    nums[index] = -nums[index]
  
  # Return duplicates list
  return duplicates