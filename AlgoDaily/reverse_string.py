def reverse_string(str1):
    for i in range(len(str1)-1):
        tempStr=''
        while len(str1)>=1:
            tempStr += str1[(len(str1)-1)]
            str1 = str1[:-1]
        str1 = tempStr
    return str1
