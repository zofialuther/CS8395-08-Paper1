

def merge(intervals):
  if len(intervals) <= 1:
    return intervals
  else:
    intervals.sort(key=lambda x: x[0])
    result = []
    newInterval = intervals[0]
    result.append(newInterval)
    for interval in intervals:
      if interval[0] <= newInterval[1]:
        newInterval[1] = max(interval[1], newInterval[1])
      else:
        newInterval = interval
        result.append(newInterval)
    return result