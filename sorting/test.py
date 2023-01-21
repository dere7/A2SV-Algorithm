# User function Template for python3

class Solution:
    def bubbleSort(self, arr, n):
        for i in range(n - 1, 0, -1):
            for j in range(i):
                if arr[j] > arr[j + 1]:
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp
    
    def insertionSort(self, arr, n):
        for i in range(1, n):
            for j in range(i, 0, -1):
                if arr[j - 1] > arr[j]:
                    temp = arr[j - 1]
                    arr[j - 1] = arr[j]
                    arr[j] = temp

    def mergeSort(self, arr, n):
        self._mergeSort(arr, start=0, end=n - 1)
    
    def _mergeSort(self, arr, start, end):
        n = end - start
        if n == 0 or n == 1:
            return
        # divide
        mid = n // 2
        self._mergeSort(arr, start=start, end=mid)
        self._mergeSort(arr, start=mid + 1, end=end)

        # conquer/merge using insertion sort
        for i in range(1, n + 1):
            for j in range(i, 0, -1):
                if arr[j - 1] > arr[j]:
                    arr[j - 1], arr[j] = arr[j], arr[j - 1]
    
    def quickSort(self, arr, n):
        self._quickSort(arr, 0, n - 1)
    
    def partition(self, arr, leftIdx, rightIdx):
        pivot = arr[rightIdx]
        i = leftIdx - 1

        for j in range(leftIdx, rightIdx):
            if arr[j] <= pivot:
                i = i + 1
                (arr[i], arr[j]) = (arr[j], arr[i])

        # swap the pivot element with the greater element specified by i
        (arr[i + 1], arr[rightIdx]) = (arr[rightIdx], arr[i + 1])

        # return the position from where partition is done
        return i + 1


    def _quickSort(self, arr, leftIdx, rightIdx):
        if leftIdx < rightIdx:
            pivotIdx = self.partition(arr, leftIdx, rightIdx)
            self._quickSort(arr, leftIdx, pivotIdx - 1)
            self._quickSort(arr, pivotIdx, rightIdx)

    def heapify(self, arr, n, i):
        # Find largest among root and children
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
    
        if l < n and arr[i] < arr[l]:
            largest = l
    
        if r < n and arr[largest] < arr[r]:
            largest = r
    
        # If root is not largest, swap with largest and continue heapifying
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)
  
  
    def heapSort(self, arr, n):
        # n = len(arr)
    
        # Build max heap
        for i in range(n//2, -1, -1):
            self.heapify(arr, n, i)
    
        for i in range(n-1, 0, -1):
            # Swap
            arr[i], arr[0] = arr[0], arr[i]
    
            # Heapify root element
            self.heapify(arr, i, 0)
  
  
# {
# Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
	n = int(input())
	arr = list(map(int, input().strip().split()))
	Solution().heapSort(arr, n)
	for i in range(n):
		print(arr[i], end=" ")
	print()
# } Driver Code Ends