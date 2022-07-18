# BRUTE FORCE REVERSE_STRING

def reverse_str(s):
    new_str = ""
    
    i = len(s)
    while i > 0:
        new_str = s[i-1]
        i = i-1
    return new_str