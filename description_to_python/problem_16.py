

def find_duplicates(arr):
    duplicates = []
    for i in range(len(arr)):
        if arr[abs(arr[i])-1] < 0:
            duplicates.append(abs(arr[i]))
        else:
            arr[abs(arr[i])-1] *= -1
    return duplicates