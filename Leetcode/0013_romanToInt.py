def romanToInt(s):
    values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
    counter= 0

    for i in range(len(s)):
        #base case: check if we're on the last one
        if i == len(s)-1:
            counter += values[s[i]]
            return counter
            
        if values[s[i+1]] > values[s[i]]:
            counter -= values[s[i]]
            
        else:
            counter += values[s[i]]