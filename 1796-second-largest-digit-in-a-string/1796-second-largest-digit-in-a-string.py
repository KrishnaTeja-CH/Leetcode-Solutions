class Solution:
    def secondHighest(self, s: str) -> int:
        num = set()
        for c in s:
            if c.isnumeric(): num.add(int(c))
        return sorted(list(num))[-2] if len(list(num)) >= 2 else -1

    