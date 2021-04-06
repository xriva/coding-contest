def solve(N,H):
    cnt=0
    for i in range(1,N-1):
        if H[i]>H[i-1] and H[i]>H[i+1]:
            cnt+=1
    return cnt

T = int(input())
for i in range(T):
    N = int(input())
    H = list(map(int, input().split()))

    print("Case #%d: %d" % (i+1, solve(N,H)))
