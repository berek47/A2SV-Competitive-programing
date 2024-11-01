import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    x = tuple(map(int, input().split()))
    ans = j = 0
    for i in range(n):
        while j < n and x[j] >= j - i + 1:
            j += 1
        ans += j - i
    print(ans)
