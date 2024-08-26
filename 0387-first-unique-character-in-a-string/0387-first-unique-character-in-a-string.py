class Solution:
    def firstUniqChar(self, s: str) -> int:
        sol = Counter(s)
        for i in s:
            if sol[i]==1:
                return s.index(i)
        return -1

        