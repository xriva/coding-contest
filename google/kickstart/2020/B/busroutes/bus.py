def solve(N,D,X):
    result=D
    for x in reversed(X):
        result = result - (result%x)
        #print(D,x,result)
    return result

T = int(input())
for i in range(T):
    N,D = map(int, input().split())
    X = list(map(int, input().split()))
    print("Case #%d: %d" % (i+1, solve(N,D,X)))
