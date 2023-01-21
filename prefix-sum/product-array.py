class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
    
        product = 1
        for i in range(n):
            answer[i] = product
            product *= nums[i]
        
        product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= product
            product *= nums[i]
        
        return answer
