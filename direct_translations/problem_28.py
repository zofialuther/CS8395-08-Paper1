

def lengthOfLongestSubstring(s):
  n = len(s)
  ans = 0
  map = {}
  for end in range(n):
    alpha = s[end]
    if alpha in map:
      start = max(map[alpha], start)
    ans = max(ans, end - start + 1)
    map[alpha] = end + 1
  return ans