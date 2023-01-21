class Solution:
    def select(self, arr, start):
        smallest = start
        n = len(arr)
        for i in range(start + 1, n):
            if arr[smallest] > arr[i]:
                smallest = i
        return smallest

    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # sorting using selection sort
        indices = []
        n = len(nums)
        for i in range(n):
            smallest = self.select(nums, i)
            if i != smallest:
                temp = nums[smallest]
                nums[smallest] = nums[i]
                nums[i] = temp
            if nums[i] == target:
                indices.append(i)
        
        return indices
