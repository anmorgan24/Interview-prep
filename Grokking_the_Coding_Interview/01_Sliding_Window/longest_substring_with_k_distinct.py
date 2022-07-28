def longest_substring_with_k_distinct(str1, k):
    window_start=0
    max_length=0
    char_frequency={}
    
    # extend the range as much as possible
    for window_end in range(len(str1)):
        right_char=str1[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1
        
        # once length of char_frequency exceeds k, shrink the window from the left 
        while len(char_frequency) > k:
            left_char = str1[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1
        max_length = max(max_length, window_end-window_start+1)
    return max_length