def possible(D,K,d):
    s = 0 
    for x in D:
        s += x//d + (1 if x%d else 0) - 1

    #print('possible:', d, s,K, D)
    return s<=K

# binary search
def bsolve(D, K, lo, hi):
    if lo==hi:
        return lo

    d = (hi+lo)//2
    if possible(D,K,d):
        return bsolve(D,K, lo, d)
    else:
        return bsolve(D,K, d+1, hi)

def solve(N,K,M):
    D = [M[i]-M[i-1] for i in range(1,N)]
    D = sorted(D, reverse=True)

    return bsolve(D, K, 1, D[0])

T = int(input())
for i in range(T):
    N,K = map(int, input().split())
    M = list(map(int, input().split()))

    print("Case #%d: %d" % (i+1, solve(N,K,M)))
