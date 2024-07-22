class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        n1 = len(s1)
        n2 = len(s2)
        dp = {}

        def f(i, j, dp):
            if (i, j) in dp:
                return dp[(i,j)]
            if i == n1 and j == n2:
                return 0
            if i == n1:
                temp = 0
                for _ in range(j, n2):
                    temp += ord(s2[_])
                return temp
            if j == n2:
                temp = 0
                for _ in range(i, n1):
                    temp += ord(s1[_])
                return temp
            if s1[i] != s2[j]:
                t1 = f(i+1, j, dp) + ord(s1[i])
                t2 = f(i, j+1, dp) + ord(s2[j])
                dp[(i,j)] = min(t1, t2)
                return dp[(i,j)]
            else:
                dp[(i,j)] = f(i+1, j+1, dp)
                return dp[(i,j)]

        return f(0, 0, dp)