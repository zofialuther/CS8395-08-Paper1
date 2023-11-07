

def reverse_number(x):
    num = str(x)
    reversed_num = int(num[::-1])
    if reversed_num > (2**31)-1:
        return 0
    else:
        return reversed_num