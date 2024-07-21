class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        diffs = [0] * (len(nums) // 2)
        for i in range(len(diffs)):
            diffs[i] = abs(nums[i] - nums[n - i - 1])
        cnts = Counter(diffs)
        most_freq_diff = 0
        diff_cnt = 0
        for diff in cnts:
            here = cnts[diff]
            if here > diff_cnt:
                diff_cnt = here
                most_freq_diff = diff
        max_to_get_1 = []
        for i in range(len(diffs)):
            here = max([abs(0 - nums[n - i - 1]),
                        abs(k - nums[n - i - 1]),
                        abs(nums[i] - 0),
                        abs(nums[i] - k)])
            max_to_get_1.append(here)
        max_to_get_1.sort()
        def helper(X):
            result = len(nums)
            result -= cnts[X]
            result -= len(diffs) - bisect.bisect_left(max_to_get_1, X)
            return result
        best = math.inf
        for x in range(k+1):
            best = min(helper(x), best)
        return best