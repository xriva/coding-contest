Z=1000000007

def findMax(S):
    n = len(S)//2
    m = len(S)%2
    A = (S[0:n])
    M = A+S[n] if m==1 else A

    if n==0:
        return False, M

    return S[-n:]>A[::-1], M



def solve(N,K,S):
    allowEqual, A = findMax(S)

    #print(allowEqual, A, S)

    X=0
    for a in A:
        X = (X*K + (ord(a)-ord('a')))%Z

    return (X+1)%Z if allowEqual else X



T = int(input())
for i in range(T):
    N,K = map(int, input().split())
    S = input().strip()
    print("Case #%d: %d" % (i+1,solve(N,K,S)))
