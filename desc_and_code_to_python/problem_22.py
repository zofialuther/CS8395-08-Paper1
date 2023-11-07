def intersect(nums1, nums2):
  nums1.sort()
  nums2.sort()
  i, j, k = 0, 0, 0
  new_arr = []
  while i < len(nums1) and j < len(nums2):
    if nums1[i] < nums2[j]:
      i += 1
    elif nums1[i] > nums2[j]:
      j += 1
    else:
      new_arr.append(nums1[i])
      i += 1
      j += 1
  return new_arr