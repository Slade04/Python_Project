def p_g(i):
    myli=[2]
    for n in range(2,i+1):
        for k in range(2,n):
            e=n/k
            if e!=int(e) and k<n-1:
                continue
            elif k==n-1 and e!=int(e):
                myli.append(n)
                continue
            else:
                break
    return myli
def goldbach(upto):
    for i1 in range(6,upto):
        times=0
        for i2 in p_g(upto):
            for i3 in p_g(upto):
                for i4 in p_g(upto):
                    if i2+i3+i4==i1:
                        times+=1
        if times==0:
            print(i1)
var=int(input('----->'))
goldbach(var)
