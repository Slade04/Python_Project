i=int(input("integer"))
print(2)
for n in range(2, i+1):
    for k in range(2, n):
        e=n/k
        if e!=int(e) and k<n-1:
            continue
        elif k==n-1 and e!=int(e):
            print(n)
            continue
        else:
            break
def p_g():
    import sys
    i = int(sys.stdin.readline())
    print(2)
    for n in range(2,i+1):
        for k in range(2,n):
            e=n/k
            if e!=int(e) and k<n-1:
                continue
            elif k==n-1 and e!=int(e):
                print(n)
                continue
            else:
                break
print(p_g())
