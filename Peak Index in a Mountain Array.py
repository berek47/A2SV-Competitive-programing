class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        i, j = 1, len(arr)-2
        while(i <= j):
            mid = i + (j-i)//2
            if(arr[mid+1] < arr[mid] > arr[mid-1]):
                return mid
            if(arr[mid+1] < arr[mid]):
                j = mid-1
            else:
                i = mid+1
