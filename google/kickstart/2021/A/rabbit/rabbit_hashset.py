
def check(R,C,r,c):
    return r in range(R) and c in range(C)

def solve(R,C,G):
    #for i in range(R):
    #    print(G[i])

    bucket = dict()
    for i in range(R):
        for j in range(C):
            x = G[i][j]
            if x not in bucket:
                bucket[x] = set()
            bucket[x].add((i,j))

    result = 0
    while len(bucket)>0:
        #print(bucket)
        x = max(bucket.keys())

        while(len(bucket[x])>0):
            r,c = bucket[x].pop()

            target = G[r][c]-1

            for i,j in [(0,1),(0,-1),(1,0),(-1,0)]:
                if check(R,C,r+i, c+j):
                    cur = G[r+i][c+j]
                    d = target - cur
                    if d>0:
                        # del cur from bucket
                        bucket[cur].remove((r+i,c+j))
                        if len(bucket[cur])==0:
                            del bucket[cur]

                        # add target into bucket
                        if target not in bucket:
                            bucket[target]=set()
                        bucket[target].add((r+i, c+j))

                        G[r+i][c+j] += d
                        result += d

        if len(bucket[x])==0:
            del bucket[x]
            

    return result
    

T = int(input())
for i in range(T):
    R,C = map(int, input().split())
    G = []
    for j in range(R):
        G.append(list(map(int, input().split())))

    print("Case #%d: %d" % (i+1, solve(R,C,G)))
