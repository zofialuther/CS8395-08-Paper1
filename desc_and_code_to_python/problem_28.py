

def lengthOfLongestSubstring(s):
  n = len(s)
  ans = 0
  map = {}
  start = 0
  end = 0
  while end < n:
    alpha = s[end]
    if alpha in map:
      start = max(map[alpha], start)
    ans = max(ans, end - start + 1)
    map[s[end]] = end + 1
    end += 1
  return ans