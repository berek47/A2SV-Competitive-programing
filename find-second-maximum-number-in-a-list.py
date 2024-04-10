if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sorted_arr = sorted(set(arr), reverse=True)
    print(sorted_arr[1])
