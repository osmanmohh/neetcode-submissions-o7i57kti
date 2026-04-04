class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for br in range(0, 9, 3):
            for bc in range(0, 9, 3):
                seen = set()
                for r in range(3):
                    for c in range(3):
                        char = board[r + br][c + bc]
                        if char == '.':
                            continue
                        if char in seen:
                            return False
                        seen.add(char)
        
        for r in range(9):
            seen = set()
            for c in range(9):
                char = board[r][c]
                if char == '.':
                    continue
                if char in seen:
                    return False
                seen.add(char)

        for c in range(9):
            seen = set()
            for r in range(9):
                char = board[r][c]
                if char == '.':
                    continue
                if char in seen:
                    return False
                seen.add(char)
        return True