def solve(K,A):
    B = [A[0]]
    for i in range(1,K):
        if A[i]!=A[i-1]:
            B.append(A[i])

    N = len(B)
    if N<=4: 
        return 0

    prevUD = B[1]>B[0]
    cnt=2

    result = 0
    for i in range(2,N):
        ud = B[i]>B[i-1]
        if ud == prevUD:
            cnt+=1
        else:
            result+=(cnt-1)//4
            prevUD = ud
            cnt=2

    result += (cnt-1)//4

    return result

T = int(input())
for i in range(T):
    K = int(input())
    A = list(map(int, input().split()))
    print("Case #%d: %d" % (i+1, solve(K,A)))
