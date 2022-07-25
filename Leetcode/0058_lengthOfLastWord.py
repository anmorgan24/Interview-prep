def lengthOfLastWord(s):
    stripped_list = [x.strip(' ') for x in s.split(' ')]
    test_list = [i for i in stripped_list if i]
    return len(test_list[-1])