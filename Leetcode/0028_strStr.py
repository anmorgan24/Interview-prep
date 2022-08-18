class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        nl, hl = len(needle), len(haystack)
        if nl == 0:
            return nl
        if hl < nl:
            return -1
        for i in range(hl-nl+1):
            if haystack[i:i+nl] == needle:
                return i
        return -1