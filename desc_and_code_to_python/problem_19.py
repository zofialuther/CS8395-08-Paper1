

def addStrings(num1, num2):
    sb = ""
    carry = 0
    i = len(num1) - 1
    j = len(num2) - 1
    while i >= 0 or j >= 0 or carry == 1:
        x = 0 if i < 0 else int(num1[i]) - ord('0')
        y = 0 if j < 0 else int(num2[j]) - ord('0')
        sb += str((x + y + carry) % 10)
        carry = (x + y + carry) // 10
        i -= 1
        j -= 1
    return sb[::-1]