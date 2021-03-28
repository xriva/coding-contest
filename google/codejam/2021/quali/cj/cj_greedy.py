def solve(X,Y,S):
    s = S.replace('?','')
    return s.count('CJ')*X + s.count('JC')*Y

T = int(input())
for i in range(T):
    X,Y,S = input().split()
    print("Case #%d: %d" % (i+1, solve(int(X), int(Y), S.strip())))
