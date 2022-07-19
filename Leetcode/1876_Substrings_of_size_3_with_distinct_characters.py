def countGoodSubstrings(s):
    count=0
    for window_start in range(len(s)):
        window_end = window_start+3
        sub_string=s[window_start:window_end]
            
        if len(set(sub_string))==3:
            count+=1
    return count