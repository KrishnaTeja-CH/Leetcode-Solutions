class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        sol = set()
        for c in count.values():
            if c in sol:
                return False
            else:
                sol.add(c)
        return True
        