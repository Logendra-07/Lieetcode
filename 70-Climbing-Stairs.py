class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=3:
            return n
        p1 = 3
        p2 = 2
        dp = 0
        for _ in range(3,n):
            dp = p1 + p2
            p2 = p1
            p1 = dp
        return dp