

def addStrings(num1, num2): 
  # Initialize the variables needed for the problem
  sb = ""
  carry = 0
  i = len(num1) - 1
  j = len(num2) - 1

  # Check if either i or j is greater than 0, or if carry is equal to 1
  while (i >= 0 or j >= 0 or carry == 1): 
    # Set x and y equal to 0 if i or j are less than 0, otherwise set them equal to the character at the index i or j for num1 and num2
    x = 0 if i < 0 else int(num1[i])
    y = 0 if j < 0 else int(num2[j])

    # Append the remainder of (x + y + carry) when divided by 10 to sb 
    sb += str((x + y + carry) % 10)

    # Set carry equal to (x + y + carry) divided by 10 
    carry = (x + y + carry) // 10

    # Decrement i and j
    i -= 1 
    j -= 1

  # Reverse and return the string from sb 
  return sb[::-1]