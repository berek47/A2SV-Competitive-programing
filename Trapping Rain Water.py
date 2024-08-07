class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = []
        rightMax = []
        result = 0 
        max_lh = 0 
        max_rh = 0  
        for i in range(len(height)):
            if i == 0:
                leftMax.append(0) 
                max_lh = max(max_lh, height[i])
            else:
                leftMax.append(max_lh)
                max_lh = max(max_lh, height[i])
        for j in range(len(height)-1, -1, -1):
            if j == len(height)-1:
                rightMax.append(0)
                max_rh = max(max_rh, height[j])
            else:
                rightMax.append(max_rh)
                max_rh = max(max_rh, height[j])
        rightMax.reverse()
        for i in range(len(leftMax)):
            val = min(leftMax[i], rightMax[i]) - height[i]
            result += val if val > 0 else 0 
        return result
