from collections import defaultdict
import sys

input = sys.stdin.readline
n = int(input())
s = tuple(input().strip())
target_unique_chars = len(set(s))

unique_count = 0
char_count = defaultdict(int)
start_index = 0
min_length = float("inf")

for end_index in range(n):
    while start_index < n and unique_count < target_unique_chars:
        unique_count += char_count[s[start_index]] == 0
        char_count[s[start_index]] += 1
        start_index += 1

    if unique_count == target_unique_chars:
        min_length = min(min_length, start_index - end_index)

    unique_count -= char_count[s[end_index]] == 1
    char_count[s[end_index]] -= 1

print(min_length)
