class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        for i in range(len(haystack)):
            if haystack[i] == needle[:1]:
                if haystack[i: i+n] == needle:
                    return i
                else:
                    i += 1
        return -1