
def sp_prost(n):
    sp=[]
    
    for i in range(2,n+1):
        f=1
        for j in range(2,i+1):
            if i%j==0 and j!=i:
                f=0
                break
                
        if f>0:
            sp.append(j)
    return sp



def somn(n):
    print(sp_prost(n))
    if n > 10:
        for i in sp_prost(n):
            if n % i ==0:
                break
        return "{:d}*{:s}".format(i,str(somn(n//i)))
    else:
         return n

print(somn(378))
