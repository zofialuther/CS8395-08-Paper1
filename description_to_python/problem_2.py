

def unique_chars(string):
  char_set = set()
  for char in string:
    if char in char_set:
      return False
    else:
      char_set.add(char)
  return True