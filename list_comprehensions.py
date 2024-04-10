if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    all = [[i, j, k] for i in range(0, x + 1) for j in range(0, y + 1)for k in range(0, z + 1)]
    ans = [arr for arr in all if sum(arr) != n]
    
    print(ans)
