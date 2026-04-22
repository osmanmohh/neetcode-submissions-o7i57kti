class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            seen = set()
            for c in range(9):
                token = board[r][c]
                if token == ".": continue
                if token in seen:
                    return False
                seen.add(token)
            
        for c in range(9):
            seen = set()
            for r in range(9):
                token = board[r][c]
                if token == ".": continue
                if token in seen:
                    return False
                seen.add(token)

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen = set()
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        token = board[r][c]
                        if token == ".": continue
                        if token in seen:
                            return False
                        seen.add(token)


        return True
        