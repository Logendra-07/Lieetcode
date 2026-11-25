class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s > 9 * n:
            return -1
        if s == 0:
            return 0
        ans = 0
        while n:
            if s >= 9:
                ans += 9
                s -= 9
            else:
                ans += s
                s = 0
            ans *= 10
            n -= 1
        return ans // 10