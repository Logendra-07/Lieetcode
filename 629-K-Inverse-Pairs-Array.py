class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (k + 1)
        dp[0] = 1  
        for i in range(1, n + 1):
            new_dp = [0] * (k + 1)
            new_dp[0] = 1
            for j in range(1, k + 1):
                val = (new_dp[j - 1] + dp[j]) % MOD
                if j >= i:
                    val = (val - dp[j - i] + MOD) % MOD
                new_dp[j] = val
            dp = new_dp
        return dp[k]