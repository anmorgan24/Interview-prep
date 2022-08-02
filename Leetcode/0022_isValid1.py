def isValid(s):
    openings = ['(', '[', '{']
    bracket_dict = {
        "(":")",
        "[":"]",
        "{":"}"
    }
    for i in range(len(s)):
        if s[i] in openings:
            if s[i+1] == bracket_dict[s[i]]:
                continue
            else:
                return False
        return True