import random
import itertools
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        target_size = 2 ** n  # we know how many subsets we need
        seen = set()

        # include empty set
        seen.add(tuple())

        while len(seen) < target_size:
            random.shuffle(nums)
            # pick a random subset length
            k = random.randint(0, n)
            # randomly sample k elements
            subset = tuple(sorted(random.sample(nums, k)))
            seen.add(subset)

        return [list(s) for s in seen]