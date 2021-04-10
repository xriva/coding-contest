def solve(N,A):
    i=0
    maxL=0
    while i<N-1:
        d = A[i+1]-A[i]
        j = i
        while j<N-1 and A[j+1]-A[j]==d:
            j+=1

        maxL = max(maxL, j-i+1)
        i = max(i+1, j)

    return maxL
            


T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print("Case #%d: %d" % (i+1, solve(N,A)))

