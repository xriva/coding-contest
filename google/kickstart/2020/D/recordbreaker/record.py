def solve(N,V):
    curMax = -1
    cnt = 0
    for i in range(N-1):
        if V[i]>curMax:
            curMax = V[i]
            if V[i]>V[i+1]:
                cnt+=1

    if V[-1]>curMax:
        cnt+=1

    return cnt


T = int(input())
for i in range(T):
    N = int(input())
    V = list(map(int, input().split()))

    print("Case #%d: %d" % (i+1, solve(N,V)))
