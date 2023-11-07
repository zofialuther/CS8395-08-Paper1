

def longest_substring_length(s):
  seen = {}
  start_index = 0
  max_length = 0
  
  for i, char in enumerate(s):
    if char in seen and start_index <= seen[char]:
      start_index = seen[char] + 1
    else:
      max_length = max(max_length, i - start_index + 1)
    
    seen[char] = i
  
  return max_length