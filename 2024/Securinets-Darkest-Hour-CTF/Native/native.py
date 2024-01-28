
def func1(a,b,c):
    return (a&b) | (a&c) | (c&b)

def func2(a,b,c):
    return a^b^c

def func3(a,b):
    if len(a)>len(b):
        return a,b+[0]*(len(a)-len(b))
    return b,a+[0]*(len(b)-len(a))

def func4(l1,l2):
    a,b=func3(l1,l2)
    res=[]
    c=0
    for i,j in zip(a,b):
        res.append(func2(i,j,c))
        c=func1(i,j,c)
    if c==1:
        res.append(c)
    return res

def func5(a,b):
    res=[0]*512
    y=a
    for i in b:
        if i==1:
            res=func4(res,y)
            if len(res)>511:
                res=res[:511]
        y=func4(y,y)
        if len(y)>511:
            y=y[:511]
    return res    
def func6(a):
    return [int(i) for i in bin(int(a.encode().hex(),16))[2:]][::-1]
message="Hello being native as possible is quite hard maybe i should use some library next time"
message=func6(message)
flag="Securinets{REDIRECT}"
flag=func6(flag)
print(func5(flag,message))
