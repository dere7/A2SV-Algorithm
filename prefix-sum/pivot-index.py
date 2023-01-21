class Solution:        
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0]
        for i in range(n):
            prefix_sum.append(prefix_sum[i] + nums[i])
        for i in range(n):
            left_sum = prefix_sum[i]
            right_sum = prefix_sum[-1] - prefix_sum[i + 1]
            if left_sum == right_sum:
                return i
        return -1
