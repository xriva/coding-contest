def fill_seg(R,C,grid):
    seg = []
    result = []
    for i in range(R):
        seg.append([])
        for j in range(C):
            if grid[i][j]==1:
                seg[i].append([1,1,1,1])
            else:
                seg[i].append(None)

    for i in range(R):
        for j in range(C):
            if seg[i][j] is not None:
                if i>0 and seg[i-1][j] is not None:
                    seg[i][j][0]+=seg[i-1][j][0]
                if j>0 and seg[i][j-1] is not None:
                    seg[i][j][1]+=seg[i][j-1][1]

    for i in range(R-1,-1,-1):
        for j in range(C-1,-1,-1):
            if seg[i][j] is not None:
                if i<R-1 and seg[i+1][j] is not None:
                    seg[i][j][2]+=seg[i+1][j][2]
                if j<C-1 and seg[i][j+1] is not None:
                    seg[i][j][3]+=seg[i][j+1][3]

                result.append(seg[i][j])
    #for i in range(R):
        #print(seg[i])
    return result

def calc_lshape(a,b):
    b -= b%2
    if b>2*a:
        return a-1
    else:
        return b//2-1

def count_lshape(node):
    n=0
    for i in range(4):
        for j in range(0,4):
            if (i%2) != (j%2) and node[i]>=2 and node[j]>=4:
                x = calc_lshape(node[i], node[j])
                #print(i,j, node, x)
                n+= x

    return n

def solve(R,C,grid):
    seg = fill_seg(R,C,grid)
    return sum([count_lshape(s) for s in seg])

T = int(input())
for i in range(T):
    R,C = map(int, input().split())
    grid = []
    for j in range(R):
        grid.append(list(map(int, input().split())))

    print("Case #%d: %d" % (i+1, solve(R,C,grid)))
