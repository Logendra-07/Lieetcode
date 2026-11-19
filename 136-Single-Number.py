class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        d=0
        for i in nums:
            d ^= i
        return d

