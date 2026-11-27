class Solution:
    def rob(self, nums: list[int]) -> int:
        n = sum = 0
        for i in nums:
            temp = max(sum, n + i)
            n = sum
            sum = temp
        return sum