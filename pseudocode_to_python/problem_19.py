

def addStrings(num1, num2):
    sb = ""
    carry = 0 
    i = len(num1) - 1
    j = len(num2) - 1
    while i >= 0 or j >= 0 or carry == 1:
        if i < 0:
            x = 0
        else:
            x = int(num1[i]) - 0
            i -= 1
        if j < 0:
            y = 0
        else:
            y = int(num2[j]) - 0
            j -= 1
        sb += str((x + y + carry) % 10)
        carry = (x + y + carry) // 10
    return sb[::-1]