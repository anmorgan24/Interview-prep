class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0 or len(words[0]) == 0:
            return []

        word_frequency = {}

        for word in words:
            if word not in word_frequency:
                word_frequency[word] = 0
            word_frequency[word] += 1

        result_indices = []
        words_count = len(words)
        word_length = len(words[0])

        for i in range((len(s) - words_count * word_length)+1):
            words_seen = {}
            for j in range(0, words_count):
                next_word_index = i + j * word_length
                # Get the next word from the string
                word = s[next_word_index: next_word_index + word_length]
                if word not in word_frequency:  # Break if we don't need this word
                    break

                # Add the word to the 'words_seen' map
                if word not in words_seen:
                    words_seen[word] = 0
                words_seen[word] += 1

                # No need to process further if the word has higher frequency than required
                if words_seen[word] > word_frequency.get(word, 0):
                    break

                if j + 1 == words_count:  # Store index if we have found all the words
                    result_indices.append(i)

        return result_indices
    

'''
Time Complexity: 
The time complexity of the above algorithm will be O(N * M * Len)
here ‘N’ is the number of characters in the given string, ‘M’ is the total number 
of words, and ‘Len’ is the length of a word.

Space Complexity:
The space complexity of the algorithm is O(M), since at most, we will be storing 
all the words in the two HashMaps. In the worst case, we also need O(N) space 
for the resulting list. So, the overall space complexity of the algorithm will be 
O(M+N).
'''