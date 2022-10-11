import random

def quick_sort(arr, begin=None, end=None):
  if begin is None:
    begin = 0
  if end is None:
    end = len(arr)
  if begin + 1 < end:
    rand_id = random.randint(begin, end - 1)
    arr[rand_id], arr[begin] = arr[begin], arr[rand_id]
    i = begin + 1
    for j in range(begin + 1, end):
      if arr[j] <= arr[begin]:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
    arr[begin], arr[i - 1] = arr[i - 1], arr[begin]
    quick_sort(arr, begin, i - 1)
    quick_sort(arr, i, end)
