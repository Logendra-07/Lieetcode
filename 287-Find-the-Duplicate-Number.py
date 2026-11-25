class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        l = 1
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            c = 0
            for num in nums:
                if num <= m:
                    c += 1
            if c > m:
                r = m
            else:
                l = m + 1
        return l