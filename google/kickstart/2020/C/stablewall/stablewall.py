def solve(R,C,M):
    # INIT
    IN=dict()
    OUT=dict()
    L = []
    S = set()
    for i in range(R):
        for j in range(C):
            S.add(M[i][j])

    # Build graph
    for j in range(C):
        for i in range(1,R):
            q = M[i][j]
            p = M[i-1][j]
            if p!=q:
                if p not in OUT:
                    OUT[p] = set()
                OUT[p].add(q)
                if q not in IN:
                    IN[q] = set()
                IN[q].add(p)
                if q in S:
                    S.remove(q)
    #print(S)

    # Topological sort
    while S:
        n = S.pop()
        L.append(n)
        #print('n:', n, 'IN:',IN, 'OUT:',OUT)
        if n not in OUT:
            continue
        while OUT[n]:
            m = OUT[n].pop()
            IN[m].remove(n)
            if not IN[m]:
                S.add(m)
                del IN[m]
        del OUT[n]

    if IN or OUT:
        return '-1'

    return ''.join(reversed(L))

T = int(input())
for i in range(T):
    R,C = map(int, input().split())
    M = []
    for j in range(R):
        M.append(input().strip())

    print("Case #%d: %s" % (i+1,solve(R,C,M)))
