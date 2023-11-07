

def add_and_reverse(num1, num2):
    carry = 0
    res = ""
    i = len(num1) - 1
    j = len(num2) - 1
    while i >= 0 or j >= 0: 
        s = carry
        if i >= 0:
            s += int(num1[i])
        if j >= 0:
            s += int(num2[j])
        res += str(s % 10)
        carry = s // 10
        i -= 1
        j -= 1
    if carry > 0:
        res += str(carry)
    return res[::-1]