class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = []
        def backtrack(start, current):
            if len(current) == len(digits):
                result.append(''.join(list(current)))
                return
            
            for letter in (digitToChar[digits[start]]):
                current.append(letter)
                backtrack(start + 1, current)
                current.pop()

        backtrack(0, [])
        return result
