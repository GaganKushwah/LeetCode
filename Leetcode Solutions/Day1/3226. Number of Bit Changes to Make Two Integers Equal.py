class Solution:
    def minChanges(self, n: int, k: int) -> int:
        nbin = bin(n)
        kbin = bin(k)
        nbin = nbin[2:]
        kbin = kbin[2:]

        if len(kbin) < len(nbin):
            for _ in range(len(nbin) - len(kbin)):
                kbin = '0' + kbin
        elif len(kbin) > len(nbin):
            for _ in range(len(kbin) - len(nbin)):
                nbin = '0' + nbin

        ans = 0
        for i in range(len(nbin)):
            if nbin[i] == kbin[i]:
                continue
            if nbin[i] == '1':
                ans += 1
            if nbin[i] == '0':
                return -1
        return ans




