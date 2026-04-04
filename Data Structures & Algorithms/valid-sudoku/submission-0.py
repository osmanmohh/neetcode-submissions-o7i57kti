class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            seen = set()
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])
        
        for c in range(9):
            seen = set()

            for r in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])            
        
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                seen = set()
                for nr in range(r,r + 3):
                    for nc in range(c, c + 3):
                        if board[nr][nc] == '.':
                            continue
                        if board[nr][nc] in seen:
                            return False
                        seen.add(board[nr][nc]) 
        return True




