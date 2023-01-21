import math
from typing import List

class Solution:
    def isCloser(self, p1: List[int], p2: List[int]) -> bool:
        # returns true if p1 is closer than p2 to the origin
        d1 = math.sqrt(p1[0] ** 2 + p1[1] ** 2)
        d2 = math.sqrt(p2[0] ** 2 + p2[1] ** 2)
        return True if d1 < d2 else False


    def heapify(self, arr, n, i):
        # Find largest among root and children
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
    
        if l< n  and self.isCloser(arr[i] , arr[l]):
            largest = l
    
        if r < n and self.isCloser(arr[largest], arr[r]):
            largest = r
    
        # If root is not largest, swap with largest and continue heapifying
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)
  
  
    def heapSort(self, arr):
        n = len(arr)
    
        # Build max heap
        for i in range(n//2, -1, -1):
            self.heapify(arr, n, i)
    
        for i in range(n-1, 0, -1):
            # Swap
            arr[i], arr[0] = arr[0], arr[i]
    
            # Heapify root element
            self.heapify(arr, i, 0)
  

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.heapSort(points)
        return [points[i] for i in range(k)]

points = [[6,10],[-3,3],[-2,5],[0,2]]
k = 3
obj = Solution()
print(obj.kClosest(points, k))
print(len(points))
