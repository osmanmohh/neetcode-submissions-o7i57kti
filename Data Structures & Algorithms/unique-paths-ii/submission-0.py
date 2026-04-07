class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m - 1][n - 1] == 1:
            return 0
        
        memo = {}
        def f(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            if (r, c) == (m - 1, n - 1):
                return 1
            if r >= m or c >= n or obstacleGrid[r][c] == 1:
                return 0
            
            memo[(r, c)] = f(r + 1, c) + f(r, c + 1)
            return memo[(r, c)]
        
        
        return f(0,0)