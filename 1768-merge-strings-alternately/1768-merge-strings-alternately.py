class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x = len(word1)
        y = len(word2)
        word3 = []
        i = j = 0
        
        while i<x or j<y:
            if i<x:
                word3.append(word1[i])
            i += 1
            
            if j<y:
                word3.append(word2[j])
            j += 1 

        return "".join(word3)
                