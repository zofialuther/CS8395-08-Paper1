

def merge_intervals(arr):
    arr.sort()
    
    merged_arr = [arr[0]]
    
    for i in range(1, len(arr)):
        if merged_arr[-1][1] >= arr[i][0]:
            merged_arr[-1][1] = max(arr[i][1], merged_arr[-1][1])
        else:
            merged_arr.append(arr[i])
    
    return merged_arr