def solve(N,A,B,C):
    # middle
    middle=([N]*C)
    left = [N-1]*A
    right = [N-1]*B
    extra = [1]*N

    N-=C
    A-=C
    B-=C

    # left
    if A<0 or A>N:
        return "IMPOSSIBLE"
    left = left[0:A]

    if B<0 or B>N:
        return "IMPOSSIBLE"
    right = right[0:B]

    #print(left, middle, right, extra)

    if A+B+C > len(extra):
        return "IMPOSSIBLE"
    elif A+B+C < len(extra):
        extra = extra[0:len(extra)-A-B-C]
        if C>1:
            return ' '.join(list(map(str,
                left + middle[0:1] + extra +  middle[1:] + right)))
        elif A>0:
            return ' '.join(list(map(str,
                left + extra + middle + right)))
        elif B>0:
            return ' '.join(list(map(str,
                left + middle + extra + right)))
        else:
            return "IMPOSSIBLE"

    else:
        return ' '.join(list(map(str,
            left + middle + right)))


T = int(input())
for i in range(T):
    N,A,B,C = map(int, input().split())
    print("Case #%d: %s" % (i+1, solve(N,A,B,C)))
