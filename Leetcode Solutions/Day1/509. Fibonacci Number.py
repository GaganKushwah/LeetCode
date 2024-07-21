class Solution:
    def fib(self, n: int) -> int:
        dp = {}

        def f(i, dp):
            if i == 0 or i == 1:
                return i
            if i in dp:
                return dp[i]
            return f(i - 1, dp) + f(i - 2, dp)

        return f(n, dp)
