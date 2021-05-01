import math
NN=1000000
def build_prime():
    isprime = [True]*(NN+1)
    i=2
    while (i*i<=NN):
        if isprime[i]:
            for j in range(i*i,NN+1,i):
                isprime[j]=False
        i+=1

    return isprime

isprime=build_prime()

def check_prime(N):
    if N<NN:
        return isprime[N]
    if N%2==0:
        return False

    for i in range(3,int(math.sqrt(N))+2,2):
        if isprime[i]:
            if N%i==0:
                return False
    return True

def solve(Z):
    if Z<15:
        return 6
    zr = int(math.sqrt(Z))
    for zr in range(zr,1,-1):
        if check_prime(zr):
            break
    #print(zr)
    zr1=zr+2
    zr2=zr-2
    for zr1 in range(zr+2,Z+1):
        if check_prime(zr1):
            break
    for zr2 in range(zr-1,1,-1):
        if check_prime(zr2):
            break

    if zr1*zr>Z:
        return zr2*zr
    else:
        return zr1*zr



T = int(input())
for i in range(T):
    Z = int(input())
    print("Case #%d: %d" % (i+1, solve(Z)))
