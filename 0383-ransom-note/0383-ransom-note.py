class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran, mag = Counter(ransomNote), Counter(magazine)
        for i in ran:
            mag[i] = mag.get(i,0)- ran[i]
            if mag[i]< 0 :
                return False
        return True
