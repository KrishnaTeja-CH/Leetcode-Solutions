class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        count = Counter(chars)
        for w in words:
            current = defaultdict(int)
            good = True
            for c in w:
                current[c] += 1
                if c not in count or current[c] > count[c]:
                    good = False
                    break
            if good:
                res += len(w)
        return res
                
        