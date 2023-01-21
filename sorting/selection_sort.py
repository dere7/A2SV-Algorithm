# User function Template for python3

class Solution:
    def select(self, arr, i):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[minimum] > arr[j]:
                minimum = j
        return minimum

    def selectionSort(self, arr, n):
        for i in range(n - 1):
            smallest = self.select(arr, i)
            if smallest != i:
                temp = arr[smallest]
                arr[smallest] = arr[i]
                arr[i] = temp


# {
# Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i], end=" ")
        print()
# } Driver Code Ends
