

def custom_sort(arr):
  arr.sort(key=lambda x:(int(x),x))
  return arr