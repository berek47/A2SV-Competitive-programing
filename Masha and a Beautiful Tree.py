def solve():
    m=int(input())
    p=[int(i)-1 for i in input().split()]
    ops=0
    while(m>1):
        arr=[]
        for i in range(0,m,2):
            if(p[i]//2!=p[i+1]//2):
                print(-1)
                return
            if(p[i]>p[i+1]):
                ops+=1
            arr.append(p[i]//2)
        m//=2
        p=arr
    print(ops)
 
 
t=int(input())
for _ in range(t):
    solve()
	 
