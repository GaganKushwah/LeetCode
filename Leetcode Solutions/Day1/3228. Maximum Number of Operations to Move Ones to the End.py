class Solution:
    def maxOperations(self, s: str) -> int:
        ar = []
        for i in range(len(s)):
            ar.append(s[i])

        boo = False
        c = 0
        ans = 0
        for i in range(len(ar)):
            if ar[i] == '1':
                c += 1
                boo = False
            if ar[i] == '0' and not boo:
                ans += c
                boo = True
        return ans








