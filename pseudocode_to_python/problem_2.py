

def is_unique(string):
  seen_characters = set()
  for character in string:
    if character in seen_characters:
      return False
    seen_characters.add(character)
  return True