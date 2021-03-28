def solve(N,L):
    result = 0
    for i in range(N-1):
        j = L[i:].index(min(L[i:]))+i
        result += j-i+1
        L = L[0:i] + list(reversed(L[i:j+1])) + L[j+1:]
        #print(i,j,L)
    return result


T = int(input())
for i in range(T):
    N = int(input())
    L = list(map(int, input().split()))

    print("Case #%d: %d" % (i+1, solve(N,L)))
