from collections import defaultdict

def solve(G):
    prog = [ ((0,1), (2,1)), 
             ((1,0), (1,2)),
             ((0,0), (2,2)),
             ((0,2), (2,0))
            ]

    #print(G)
    result = defaultdict(int)
    for p,q in prog:
        #print(p,q)
        x = G[p[0]][p[1]] + G[q[0]][q[1]]
        if (x%2)==0:
            result[x//2]+=1

    value = list(sorted(result, key=lambda x: result[x]))
    #print(value)
    if value:
        x = result[value[-1]]
    else:
        x =0

    for i in [0,2]:
        if G[i][0] + G[i][2] == G[i][1]*2:
            x+=1

    for i in [0,2]:
        if G[0][i] + G[2][i] == G[1][i]*2:
            x+=1

    return x
       

T = int(input())
for i in range(T):
    G = []
    for j in range(3):
        G.append(list(map(int, input().split())))

    G[1].append(G[1][1])

    print("Case #%d: %d" % (i+1, solve(G)))
