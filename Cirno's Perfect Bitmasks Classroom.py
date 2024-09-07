for _ in range(int(input())):
    n = int(input())
    ans = n & (-n) 
    if ans != n:
        print(ans)
    else:
        if n == 1:
            print(ans + 2) 
        else:
            print(ans + 1) 
