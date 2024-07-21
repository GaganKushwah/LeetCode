class Solution:
    def minimumLength(self, s: str) -> int:
        from collections import Counter
        m = Counter(s)
        print(m)
        x = 0
        for count in m.values():
            y = count - 1
            x += y % 2
            x+=1
        return x