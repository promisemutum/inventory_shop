def mRNA(x):
    lst=[]
    b=''
    for i in x:
        if i=='G':
            lst.append('C')
        elif i=='C':
            lst.append('G')
        elif i=='T':
            lst.append('A')
        elif i=='A':
            lst.append('U')
        else:
            print("Invalid")
    return (b.join(lst))

a="GCTAATC"
print(mRNA(a))
