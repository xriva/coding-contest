def solve(N,K,S):
    k = sum([1 if S[i]!=S[-1-i] else 0 for i in range(N//2)])
    return abs(k-K)

T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    S = input().strip()
    print("Case #%d: %d" % (i+1, solve(N,K,S)))
