if __name__ == '__main__':
    n = int(input())
    arr = sorted(set(map(int, input().split())))[-2]
    print(arr)