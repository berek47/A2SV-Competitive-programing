class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def backtrack(start, path):
            if start == len(num):
                return len(path) >= 3
            
            for end in range(start + 1 , len(num) + 1):
                current_str = num[start: end]
                if len(current_str) > 1 and current_str[0] == '0':
                    continue
                current_num = int(current_str)
                if len(path) < 2 or current_num == path[-1] + path[-2]:
                    if backtrack(end, path + [current_num]):
                        return True
            
            return False
        

        return backtrack(0, [])
