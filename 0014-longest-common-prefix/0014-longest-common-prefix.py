class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        start = strs[0]
        for i in strs:
            while not i.startswith(start):
                start = start[:-1]
        return start
        