class Solution:
    def secondHighest(self, s: str) -> int:
        num = []
        for c in s:
            if c.isnumeric(): num.append(int(c))
        return sorted(list(set(num)))[-2] if len(list(set(num))) >= 2 else -1

    