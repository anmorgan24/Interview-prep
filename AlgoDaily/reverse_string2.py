def reverse_string(str1):
    str1 = [char for char in str1]
    position = 0
    for x in range(len(str1)-1):
        str1.insert(position, str1[len(str1)-1])
        str1= str1[:-1]
        position += 1
    return ''.join(str1)
    
