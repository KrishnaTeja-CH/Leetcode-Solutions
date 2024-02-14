class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = []
        for w in words:
            for c in w:
                if chars.count(c) < w.count(c):
                    break
            else:
                res.append(len(w))
        return sum(res)
                    
                
        