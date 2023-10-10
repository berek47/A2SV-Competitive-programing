class Solution:
    def select(self, arr, i):
        # code here
        min = i
        j=i
        for j in range(i, len(arr)):
            if arr[j] < arr[min]:
                min = j

        return min

    def selectionSort(self, arr, n):
        # code here
        i = 0
        while i < len(arr):
            min = self.select(arr, i)

            arr[min], arr[i] = arr[i], arr[min]
            i += 1
        return arr
