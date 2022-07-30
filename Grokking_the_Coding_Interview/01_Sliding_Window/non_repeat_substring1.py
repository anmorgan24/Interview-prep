def non_repeat_substring(str1):
  
  window_start = 0
  max_length = 0
  window_chars=[]

  for window_end in range(len(str1)):
    window_chars.append(str1[window_end])

    while len(window_chars) != len(set(window_chars)):
      window_chars.pop(0)
      window_start += 1

    max_length = max(max_length, window_end-window_start+1)

  return max_length