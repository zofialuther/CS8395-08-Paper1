

def isAnagram(s, t):
  if len(s) != len(t):
    return False

  counter = [0] * 26
  for i in range(len(s)):
    counter[ord(s[i]) - ord('a')] += 1
    counter[ord(t[i]) - ord('a')] -= 1
  
  for count in counter:
    if count != 0:
      return False
  
  return True