class Solution:
    #Let n = len(ranges)!
    #Time-Complexity: O(nlogn + n * 1 + n * 1) - > O(nlogn)
    #Space-Complexity: O(n), if there are n intervals side by side non overlapping!
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        #Approach: I will iterate through each range 1-d array element in order to 
        #find all inclusive ranges that are distinct!
        
        #Then, I will iterate through each and every inclusive range and see if both left and right
        #interval within values are all contained in at least one of such ranges! 
        
        #If so, I return T! Otherwise, I return F!
        
        #We can extend the last interval inserted if its end value is off by no more than 1 compared
        #to current interval we are iterating on! -> This way I can utilize prefix sum technique
        #to extend already inserted array!
        
        
        #sort by the start point of each range first!
        ranges.sort(key = lambda x: x[0])
        
        inclusive_arr = []
        
        #initially, add the first interval!
        inclusive_arr.append(ranges[0])
        
        for i in range(1, len(ranges)):
            cur = ranges[i]
            cur_start = cur[0]
            last = inclusive_arr[-1]
            last_end = last[1]
            
            #if current interval start comes before the most recently inserted range's end value!
            if(cur_start <= last_end):
                if(cur[1] > last_end):
                    inclusive_arr[-1][1] = cur[1]
                    continue
                #if current interval end point is encompassed within already existing interval, then
                #simply don't modify most recently inserted interval!
                else:
                    continue
            else:
                #if current interval's start value is no more than 1 greater than most recently
                #inserted interval's last value, then we can simply extend the already inserted one!
                if(abs(cur_start - last_end) <= 1):
                    inclusive_arr[-1][1] = cur[1]
                    continue
                #otherwise, add on a new inclusive array!
                else:
                    inclusive_arr.append(cur)
        
                    
                
            
        
        #then, we have to check if [left, right] is contained in at least one such interval!
        
        for inc_arr in inclusive_arr:
            inc_start, inc_end = inc_arr[0], inc_arr[1]
            
            if((inc_start <= left <= inc_end) and
               (inc_start <= right <= inc_end)):
                return True
        return False
