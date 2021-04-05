def solve(N,B,A):
    s = 0
    n = 0
    for a in sorted(A):
        if s+a<=B:
            s+=a
            n+=1
        else:
            break

    return n



T = int(input())
for i in range(T):
    N,B = map(int, input().split())
    A = list(map(int, input().split()))

    print("Case #%d: %d" % (i+1, solve(N,B,A)))
