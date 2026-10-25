d=eval(input("Input a Decimal Interger: "))
r=''
f=''
if "." in str(d):
    a=str(d).split(".")
    q=int(a[0])
    m=int(a[1])
    l=len(a[1])
    n=0
    while q!=0:
        r=str(q%16)+r
        q=q//16
    while (m%(10**l))!=0 ^ n<4:
        m=m*16
        f=f+str(m//10**l)
        m=m%10**l
        b=r+'.'+f
        n+=1
    print(b)
else:
    q=int(d)
    while q!=0:
        b=str(q%16)+b
        q=q//16
    print(b)
