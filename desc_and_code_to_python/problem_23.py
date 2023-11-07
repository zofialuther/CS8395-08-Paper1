

def merge(intervals):
  if len(intervals) <= 1:
    return intervals
  intervals.sort(key=lambda x: x[0])
  result = [intervals[0]]
  new_interval = intervals[0]
  for i in intervals:
    if i[0] <= new_interval[1]:
      new_interval[1] = max(new_interval[1], i[1])
    else:
      new_interval = i
      result.append(new_interval)
  return result