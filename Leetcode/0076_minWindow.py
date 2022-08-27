def find_substring(s, t):
    window_start, matched, substr_start = 0, 0, 0
    min_length = len(s) + 1
    char_frequency={}
    
    for chr in t:
        if chr not in char_frequency:
            char_frequency[chr] = 0
        char_frequency[chr] += 1

    # 1/ Our goal is to matchall the characters from the 'char_frequency'
    # with the current window
    # 2/ Try to extend the range [window_start, window_end] as much as possible
    for window_end in range(len(s)):
        right_char = s[window_end]
        
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            
            # count every match of a character
            if char_frequency[right_char] >= 0:
                matched +=1

        # shrink the window if we can, finish as soon as we remove a matched character
        while matched == len(t):
            if min_length > window_end - window_start + 1:
                min_length = window_end - window_start + 1
                substr_start = window_start       
        
            left_char = s[window_start]
            window_start += 1

            if left_char in char_frequency:
                # Note that we could have redundany matching characters, therefore we'll decrememnt
                # the matched count only when a useful occurence of a matched character is going 
                # out of the window
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1
        
    if min_length > len(s):
        return ""
    return s[substr_start:substr_start + min_length]

# Time complexity: O(M + N), when N and M are the number of characters in the input string and pattern, 
# respectively

# Space complexity: O(M), since, in the worst case, the whole pattern can have distinct characters
# that will go into the HashMap char_frequency 