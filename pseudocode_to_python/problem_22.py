

def union_arrays(nums1, nums2): 
  i, j, k = 0, 0, 0
  nums1.sort()
  nums2.sort()
  while i < len(nums1) and j < len(nums2):
    if nums1[i] < nums2[j]:
      i += 1
    elif nums1[i] > nums2[j]:
      j += 1
    else:
      nums1[k] = nums1[i]
      i += 1
      j += 1
      k += 1
  return nums1[:k]