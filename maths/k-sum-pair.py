class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        operations = i = 0
        while i < n:
            for j in range(i + 1, n):
                if nums[i] + nums[j] == k:
                    operations += 1
                    nums[j], nums[i + 1] = nums[i + 1], nums[j]
                    i += 1
                    break
            i += 1
        return operations
