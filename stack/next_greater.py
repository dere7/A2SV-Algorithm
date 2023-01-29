from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        answer = [-1] * len(nums1)
        for num in nums2:
            while len(stack) != 0 and num > stack[-1]:
                val = stack.pop()
                for i in range(len(nums1)):
                    if nums1[i] == val:
                        answer[i] = num
            stack.append(num)
        return answer