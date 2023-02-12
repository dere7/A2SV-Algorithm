from typing import List

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        seats = [0]*(n+1)
        for booking in bookings:
            seats[booking[0]-1] += booking[2]
            seats[booking[1]] -= booking[2]
        running_sum = 0
        for i in range(n):
            running_sum += seats[i]
            seats[i] = running_sum
        return seats[:n]