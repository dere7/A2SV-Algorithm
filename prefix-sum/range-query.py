class NumArray:
	def __init__(self, nums):
		self.nums = nums
		self.prefix_sum = [0]
		for i in range(len(nums)):
			self.prefix_sum.append(self.prefix_sum[i] + nums[i])

	def sumRange(self, left: int, right: int) -> int:
		return self.prefix_sum[right + 1] - self.prefix_sum[left]
	

nums = [-2,0,3,-5,2,-1]
obj = NumArray(nums)
print(obj.sumRange(0, 2) )
print(obj.sumRange(2, 5) )
print(obj.sumRange(0, 5) )
