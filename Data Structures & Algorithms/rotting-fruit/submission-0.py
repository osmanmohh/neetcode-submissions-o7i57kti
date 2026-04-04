class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        fresh = 0
        time = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c, 0))  # (row, col, time)
                elif grid[r][c] == 1:
                    fresh += 1
            
        while q:
            for _ in range(len(q)):
                row, col, time = q.popleft()
                for dr, dc in dirs:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr, nc, time + 1))
                        fresh -= 1

        return time if fresh == 0 else -1