def solve(N,K,A):
    result = 0
    for i in range(N-K+1):
        if A[i]==K:
            isOK=True
            for j in range(1,K):
                if A[i+j]!=K-j:
                    isOK=False
                    break
            if isOK:
                result+=1

    return result


T = int(input())
for i in range(T):
    N,K = map(int, input().split())
    A = list(map(int, input().split()))
    print("Case #%d: %d" %(i+1, solve(N,K,A)))

