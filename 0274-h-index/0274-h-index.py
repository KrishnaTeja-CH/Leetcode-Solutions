class Solution:
    def hIndex(self, citations: List[int]) -> int:
        res = 0
        citations = sorted(citations, reverse = True)
        for i, j in enumerate(citations):
            res = max(res, min(j, i+1))
        return res
                