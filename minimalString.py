from collections import Counter
s = input()
remain = Counter(s)
t = []
u = []
 
for c in s:
    t.append(c)
    remain[c] -= 1
 
    if remain[c] == 0:
        del remain[c]
 
    if remain:
        while t and min(remain) >= t[-1]:
            u.append(t.pop())
    else:
        while t:
            u.append(t.pop())
print(''.join(u))
