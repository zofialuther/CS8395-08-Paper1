

def sumAdjacentKeys(arr):
    result = 0
    hmap = {}

    # Iterate through array and add each value to the HashMap 
    # and increase the count for each value stored in the HashMap
    for x in arr: 
        if x in hmap: 
            hmap[x] += 1
        else: 
            hmap[x] = 1

    # Iterate through the keys of the HashMap and if the adjacent 
    # key exists, update result to maximum of current result and 
    # the sum of the number of values from the two adjacent keys
    for k in hmap:
        if k+1 in hmap:
            result = max(result, hmap[k] + hmap[k+1])
    return result