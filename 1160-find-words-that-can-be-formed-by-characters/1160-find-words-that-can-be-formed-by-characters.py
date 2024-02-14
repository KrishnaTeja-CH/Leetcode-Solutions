class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        for w in words:
            for c in w:
                if chars.count(c) < w.count(c):
                    break
            else:
                res += len(w)
        return res
                    
                
        