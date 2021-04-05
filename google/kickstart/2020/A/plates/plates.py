def solve_recur(result,K,P,B,M):
    if (P,M) in result:
        return result[(P,M)]

    if P==0:
        result[(P,M)]=0
        return 0

    if len(B)==1:
        if P>K:
            result[(P,M)] = 0
            return 0
        result[(P,M)] = B[0][P-1]
        return B[0][P-1]

    x = solve_recur(result,K,P,B[1:],M+1)
    #print('result0:', P,0, x)
    for i in range(min(P,K)):
        y = solve_recur(result,K,P-i-1, B[1:], M+1) + B[0][i]
        #print('resulti:', P,i+1, y)
        if y>x:
            x = y

    result[(P,M)] = x
    return x


def solve(N,K,P,B):

    # accum sum
    for i in range(N):
        for j in range(1,K):
            B[i][j] += B[i][j-1]

    # cache
    result=dict()

    # recur
    return solve_recur(result,K,P,B, 0)


T = int(input())
for i in range(T):
    N,K,P = map(int, input().split())
    B = []
    for j in range(N):
        B.append(list(map(int, input().split())))


    print("Case #%d: %d" % (i+1, solve(N,K,P,B)))

