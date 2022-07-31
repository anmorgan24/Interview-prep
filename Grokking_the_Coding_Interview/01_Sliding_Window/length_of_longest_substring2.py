def length_of_longest_substring(str1, k):
    
  window_start, max_length, max_repeat_letter_count = 0, 0, 0
  frequency_map= {}

  for window_end in range(len(str1)):
    if str1[window_end] not in frequency_map:
      frequency_map[str1[window_end]]=0
    frequency_map[str1[window_end]] += 1

    max_repeat_letter_count = max(max_repeat_letter_count, frequency_map[str1[window_end]])

    if (window_end-window_start + 1-max_repeat_letter_count) > k:
      frequency_map[str1[window_start]] -= 1
      window_start += 1

    max_length = max(max_length, window_end-window_start +1)

  return max_length