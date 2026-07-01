class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       exists=any(target in row for row in matrix)
       return exists
            