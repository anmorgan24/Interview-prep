def length_of_longest_numeric_substring(arr, k):
  window_start, max_length, max_ones_count = 0, 0, 0

  for window_end in range(len(arr)):
    if arr[window_end] == 1:
      max_ones_count +=1

    if (window_end - window_start + 1 - max_ones_count) > k:
      if arr[window_start] == 1:
        max_ones_count -= 1
      window_start += 1

    max_length = max(max_length, window_end-window_start + 1)

  return max_length