

def merge(intervals):
  # Check if length of intervals is less than or equal to 1
  if(len(intervals) <= 1):
    return intervals

  # Sort intervals based on first element of each interval
  intervals.sort(key=lambda x: x[0])

  # Create a list of integers to store result
  result = []

  # Create newInterval array and assign first interval of intervals to it
  newInterval = intervals[0]

  # Add newInterval to result
  result.append(newInterval)

  # Iterate through intervals
  for interval in intervals:
    # Check if first element of interval is less than or equal to last element of newInterval
    if(interval[0] <= newInterval[1]):
      # IF true, update last element of newInterval to largest of the two
      newInterval[1] = max(newInterval[1], interval[1])
    # ELSE, assign interval to newInterval and add it to result
    else:
      newInterval = interval
      result.append(newInterval)
  
  # Return result as 2D array of integers
  return result