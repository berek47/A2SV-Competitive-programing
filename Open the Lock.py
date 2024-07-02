class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        num_options = ['0','1','2','3','4','5','6','7','8','9']
        dead_ends = set(deadends)
        if '0000' in dead_ends:
            return -1
        dead_ends.add('0000')
        queue = deque(['0000'])
        steps = 0
        while queue:
            queue_length = len(queue)
            for _ in range(queue_length):
                current_lock = queue.popleft()
                if current_lock == target:
                    return steps
                for i in range(4):
                    current_digit = int(current_lock[i])
                    next_lock_inc = current_lock[:i] + num_options[(current_digit+1)%10] + current_lock[i+1:]
                    next_lock_dec = current_lock[:i] + num_options[current_digit-1] + current_lock[i+1:]
                    if next_lock_inc not in dead_ends:
                        queue.append(next_lock_inc)
                        dead_ends.add(next_lock_inc)
                    if next_lock_dec not in dead_ends:
                        queue.append(next_lock_dec)
                        dead_ends.add(next_lock_dec)
            steps += 1
        return -1
