class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s = Counter(ransomNote)
        m = Counter(magazine)
        for i in s:
            m[i] = m.get(i, 0) - s[i]
            if m[i] < 0:
                return False
        return True
        