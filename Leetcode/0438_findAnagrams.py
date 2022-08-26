def findAnagrams(str1, pattern):
    window_start=0
    matched=0
    char_frequency={}
    
    for chr in pattern:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1


    result_indices = []
    # 1/ Our goal is to match all the characters from the 'char_frequency'
    # with the current window
    # 2/ Try to extend the range [window_start, window_end] as much as possible
    for window_end in range(len(str1)):
        right_char=str1[window_end]
        
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            
            if char_frequency[right_char] == 0:
                matched +=1

        if matched == len(char_frequency):
            result_indices.append(window_start)
        
        # shrink the window by one character 
        if window_end >= len(pattern) - 1:
            left_char = str1[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1
        
    return result_indices

# Time complexity: O(M + N), when N and M are the number of characters in the input string and pattern, 
# respectively

# Space complexity: O(M), since, in the worst case, the whole pattern can have distinct characters
# that will go into the HashMap char_frequency 
