class Solution:
    def tribonacci(self, n: int) -> int:
        dp = {}
        def f(i, dp):
            if i==0 or i==1:
                return i
            if i == 2:
                return 1
            if i in dp:
                return dp[i]
            dp[i] = f(i-1, dp) + f(i-2, dp) + f(i-3, dp)
            return dp[i]
        return f(n, dp) 