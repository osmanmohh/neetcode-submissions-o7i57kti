class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        seen = collections.defaultdict(list)
        sites = collections.defaultdict(int)
        z = list(zip(username, timestamp, website))
        z.sort(key=lambda x: x[1])
        username, timestamp, website = zip(*z)
        print(z)

        for user, time, site in zip(username, timestamp, website):
            seen[user].append(site)

        for user, history in seen.items():
            if len(history) < 3:
                continue
            l = 0
            for r in range(3, len(history)+1):
                sites[tuple(history[l:r])] += 1
                l += 1

        mostFreq = 0
        best = None
        for pattern, freq in sites.items():
            if freq >= mostFreq:
                mostFreq = freq
                if not best:
                    best = pattern
                else:
                    best = min(best, pattern)
        return list(best)






