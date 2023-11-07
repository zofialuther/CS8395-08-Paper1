

def maxLengthHarmoniousSubsequence(arr):
    result = 0
    num_map = {}
    
    for num in arr:
        if num not in num_map:
            num_map[num] = 0
        num_map[num] += 1
        
    for key in num_map:
        if key + 1 in num_map:
            result = max(result, num_map[key] + num_map[key + 1])
    return result