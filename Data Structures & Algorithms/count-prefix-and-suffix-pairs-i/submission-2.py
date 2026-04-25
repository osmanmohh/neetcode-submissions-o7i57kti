class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2):
            print(str1, str2)

            if len(str1) > len(str2):
                return False
            n = len(str1)
            return str2[len(str2) - n:] == str1 and str2[:n] == str1
        
        count = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1
        return count