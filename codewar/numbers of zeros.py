def zeros(n):
    res=0
    if n==4:return 2
    if n<5:
        return 0
    else:
        while n>4:
            n=n/5
            res=res+n
    return res
print zeros(10)


#edition2.7