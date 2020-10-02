def gcd(a,b):
    while b>0:
        #q=a//b
        r= a%b
        print("%d = %d * %d + %d  gcd(%d,%d)" %(a,a//b,b,r,b,r))
        a=b
        b=r
    print("gcd = %d" %(a))

# gcd(3768,1701)
    