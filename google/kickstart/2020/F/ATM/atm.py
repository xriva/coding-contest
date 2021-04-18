from collections import defaultdict
def solve(N,X,A):
    temp = defaultdict(list)
    for i in range(N):
        n = (A[i]-1)//X
        temp[n].append(str(i+1))

    result =[]
    for k in sorted(temp.keys()):
        result.extend(temp[k])
    return ' '.join(result)

T = int(input())
for i in range(T):
    N,X = map(int, input().split())
    A = list(map(int, input().split()))
    print("Case #%d: %s" % (i+1, solve(N,X,A)))
