def wordPattern(self, pattern):
    word_dict= {}
        
    if len(pattern) != len(s.split(" ")) or len(set(pattern)) != len(set(s.split(" "))):
        return False
    for word, letter in list(zip(pattern, s.split(" "))):
        if word_dict.get(letter):
            if word != word_dict[letter]:
                return False 
        else:
            word_dict[letter] = word
    return True