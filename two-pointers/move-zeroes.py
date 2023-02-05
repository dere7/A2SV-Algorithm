from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        end = len(nums) - 1
        start = end - 1
        while start >= 0:
            if nums[start] == 0:
                i = start
                while i < end:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    i += 1
                end -= 1
            start -= 1