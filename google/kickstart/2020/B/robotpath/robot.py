Z=1000000000

def solve(P):
    r,c = 0,0
    m = 1
    stack = []

    for x in P:
        if   x == 'E':
            c+=1
        elif x == 'W':
            c-=1
        elif x == 'S':
            r+=1
        elif x == 'N':
            r-=1
        elif x == '(':
            stack.append((r,c,m))
            #print('push', r,c, m)
            r,c=0,0
        elif x == ')':
            r0,c0,m0 = stack.pop()
            r = r0+r*m0
            c = c0+c*m0
            #print('pop ', r0,c0, m, r,c)
        else:
            m = int(x)

    return (c+Z)%Z+1, (r+Z)%Z+1

T = int(input())
for i in range(T):
    P = input().strip()
    print("Case #%d: %d %d" % (i+1, *solve(P)))
