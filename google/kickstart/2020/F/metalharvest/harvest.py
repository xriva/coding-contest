from bisect import bisect

def solve(N,K,SE):
    i=0
    cnt=0
    x = SE[0][0]
    while i<N:
        r = SE[i][1]-x
        t = r//K + (1 if r % K else 0)
        cnt+=t
        y = x+K*t

        j = bisect(SE,(y,0))-1
        if y>=SE[j][1]:
            i = j+1
            if i<N:
                x = SE[i][0]
        else:
            x = y
            i = j

    return cnt

T = int(input())
for i in range(T):
    N,K = map(int, input().split())
    SE = []
    for j in range(N):
        s,e = map(int, input().split())
        SE.append((s,e))

    print("Case #%d: %d" % (i+1, solve(N,K,sorted(SE))))
