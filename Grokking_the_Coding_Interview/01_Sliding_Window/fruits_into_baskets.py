def fruits_into_baskets(fruits):
  window_start = 0
  max_length = 0
  fruit_frequency = {}

  for window_end in range(len(fruits)):
    right_fruit = fruits[window_end]
    if right_fruit not in fruit_frequency:
      fruit_frequency[right_fruit] = 0
    fruit_frequency[right_fruit] += 1

    while len(fruit_frequency) > 2:
      left_fruit = fruits[window_start]
      fruit_frequency[left_fruit] -= 1
      if fruit_frequency[left_fruit] ==0:
        del fruit_frequency[left_fruit]
      window_start += 1
    
    max_length = max(max_length, window_end- window_start +1)

  return max_length