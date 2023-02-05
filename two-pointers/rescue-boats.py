from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people = sorted(people)
        start, end = 0, n - 1
        boats = 0
        while start <= end:
            boats += 1
            if people[start] + people[end] <= limit:
                start += 1
            end -= 1
        return boats

peoples = [5,1,4,2]
print(Solution().numRescueBoats(peoples, 6))