class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1], [1, 1], [1, 2, 1]]
        if numRows <= 3:
            return res[:numRows]
        
        for i in range(4, numRows+1):
            prev = res[-1]
            print(prev)
            new = [1] * i
            print(new)
            for j in range(1, i-1):
                new[j] = prev[j] + prev[j - 1]
            res.append(new)
        return res

