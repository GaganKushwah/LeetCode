class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = {}

        def lolz(i, cost, n, dp):

            if i >= n:
                return 0
            if i in dp:
                return dp[i]
            dp[i] = cost[i] + min(lolz(i + 1, cost, n, dp), lolz(i + 2, cost, n, dp))
            return dp[i]

        return min(lolz(0, cost, n, dp), lolz(1, cost, n, dp))