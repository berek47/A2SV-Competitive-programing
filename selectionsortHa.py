# User function Template for python3

class Solution: 
    def select(self, arr, i):
        # Find the index of the minimum element in the unsorted part
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        return min_index

    def selectionSort(self, arr, n):
        # Perform selection sort
        for i in range(n):
            # Find the minimum element in remaining unsorted array
            min_index = self.select(arr, i)
            # Swap the found minimum element with the first element of the unsorted part
            arr[i], arr[min_index] = arr[min_index], arr[i]
