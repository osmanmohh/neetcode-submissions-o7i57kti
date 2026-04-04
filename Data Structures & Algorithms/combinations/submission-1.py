class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        result = []
        def backtrack(start, current):
            # 1. Base case — record current subset
            if len(current) == k:
                result.append(list(current))

            for i in range(start, n + 1):


                # 2b. Make choice
                current.append(i)

                # 2c. Recurse
                backtrack(i + 1, current)

                # 2d. Undo choice (backtrack)
                current.pop()


        backtrack(1, [])
        return result
