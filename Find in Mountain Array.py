# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def get_mountain_idx(self, mountain_arr):
        i = 0
        j = mountain_arr.length() -1
        mid = 1
        while(i<=j):
            mid = int(i + (j-i)/2)
            val = mountain_arr.get(mid)
            val_prev = mountain_arr.get(mid-1) if mid-1>0 else -1
            val_next = mountain_arr.get(mid+1) if mid+1<mountain_arr.length() else -1
            if val_prev < val and val_next < val:
                return mid
            elif val_prev < val and val_next > val:
                i = mid+1
            else:
                j = mid-1

    def get_idx(self, i, j, mountain_arr, target, is_reverse):
        while i<=j:
            mid = int(i + (j-i)/2)
            val =  mountain_arr.get(mid)
            if val == target:
                return mid
            if  val > target and not is_reverse:
                j = mid -1
            else:
                i = mid+1
        return -1         

    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        m_idx = self.get_mountain_idx(mountain_arr)
        if mountain_arr.get(m_idx) == target:
            return m_idx
        
        m_idx = self.get_idx(0, m_idx-1, mountain_arr, target, False)

        if m_idx != -1:
            return m_idx

        m_idx = self.get_idx(m_idx-1, mountain_arr.length()-1, mountain_arr, target, True)
        

        return m_idx
