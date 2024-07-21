class Solution:
    def doesAliceWin(self, s: str) -> bool:
        dic = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
        n = 0
        for i in range(len(s)):
            if s[i] in dic:
                n += 1
        if n == 0:
            return False
        return True
