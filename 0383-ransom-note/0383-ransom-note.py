class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        k = Counter(ransomNote)
        t = Counter(magazine)
        for i in k:
            t[i] = t.get(i, 0) - k[i]
            if t[i] < 0:
                return False
        return True
        print(t[i])