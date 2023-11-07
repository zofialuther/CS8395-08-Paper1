

def areOccurrencesEqual(s):
  char_counts = {}
  for c in s:
    if c in char_counts:
      char_counts[c] += 1
    else:
      char_counts[c] = 1
  count = -1
  for c in char_counts.values():
    if count == -1:
      count = c
    elif count != c:
      return False
  return True