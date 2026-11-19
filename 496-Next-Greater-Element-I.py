class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        for target in nums1:
            ng = -1
            target_found = False
            for num in nums2:
                if num == target:
                    target_found = True
                elif target_found:
                    if num > target:
                        ng = num
                        break
            res.append(ng)
        return res