if __name__ == '__main__':
    xx = int(input())
    yy = int(input())
    zz = int(input())
    n = int(input())
    coords = [[x, y, z] for x in range(xx+1) for y in range(yy+1) for z in range(zz+1) if x+y+z!=n ]
    print(coords)