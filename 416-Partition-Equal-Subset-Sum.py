class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        half = s // 2
        dp = 1
        for num in nums:
            dp |= dp << num
        return bool((dp >> half) & 1)