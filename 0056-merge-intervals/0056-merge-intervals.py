class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals)< 2: return intervals
        intervals.sort()
       
        res = [intervals[0]]
        for i, j in intervals:
            if i > res[-1][1]:
                res.append([i,j])
            elif j > res[-1][1]:
                res[-1][1] = j
        return res

                        