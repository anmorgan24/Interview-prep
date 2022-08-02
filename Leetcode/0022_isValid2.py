def isValid(s):
    for i in range(len(s)):
        if "()" in s:
            s=s.replace("()","")
            print(s)
        if "[]" in s:
            s=s.replace("[]","")
            print(s)
        if "{}" in s:
            s=s.replace("{}","")
            print(s)
    if s == "":
        return True
    else:
        return False