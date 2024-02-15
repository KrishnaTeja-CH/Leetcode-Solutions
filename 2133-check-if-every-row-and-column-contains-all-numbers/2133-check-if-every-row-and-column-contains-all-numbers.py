class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i in matrix:
            if len(set(i))!= n:
                return False
        for i in zip(*matrix):
            if len(set(i))!= n:
                return False
        return True
        