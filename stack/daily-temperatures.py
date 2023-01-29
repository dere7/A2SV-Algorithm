from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        answer = [0] * n
        for i in range(n):
            t = temperatures[i]
            while stack and stack[-1][0] < t:
                value, idx = stack.pop()
                answer[idx] = i - idx
            stack.append((t, i))
        return answer


temperatures = [89,62,70,58,47,47,46,76,100,70]
obj = Solution()
print(temperatures)
print(obj.dailyTemperatures(temperatures))
print([8,1,5,4,3,2,1,1,0,0])