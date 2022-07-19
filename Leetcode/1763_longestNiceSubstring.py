class Solution:
    def isNice(self, s: str) -> bool:
        
        for c in s:
            if c.swapcase() not in s:
                return False
        return True
    
    def longestNiceSubstring(self, s: str) -> str:
        
        if len(s) <= 1:
            return ""
        
        if self.isNice(s):
            return s
        
        temp=''
        
        for start in range(len(s)):
            for end in range(start+1, len(s)):
                if self.isNice(s[start:end+1]):
                    temp = s[start:end+1] if len(s[start:end+1]) > len(temp) else temp
                    
        return temp