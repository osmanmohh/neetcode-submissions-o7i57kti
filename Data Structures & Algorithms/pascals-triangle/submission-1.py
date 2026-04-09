class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        for i in range(numRows-1):

            prev = res[-1]
            print(prev)
            new = [1]
            for j in range(1, len(prev)):
                new.append(prev[j] + prev[j - 1])
            new.append(1)
            print(new)
            res.append(new)
        return res
