import sys
input = sys.stdin.readline

n, s = map(int, input().strip().split())
a = list(map(int, input().strip().split()))

l, r, cur, best = 0, -1, 0, 0

while max(l, r) < n:
    if cur <= s:
        best = max(best, r - l + 1)
        r += 1
        if r < n:
            cur += a[r]
    else:
        cur -= a[l]
        l += 1

print(best)
