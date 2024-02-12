class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: 
        start = strs[0]
        for i in strs:
            print(i)
            while not i.startswith(start):
                start = start[:-1]
                print(start)
        return start