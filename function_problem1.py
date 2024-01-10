def myfunc(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    else:
        return max(a,b)
    

#print(myfunc(8,9))


def myfunc1(string):
    l1=string.lower().split()
    if l1[0][0]==l1[1][0]:
        return True
    else:
        return False


#print(myfunc1('hello how'))


def myfunc2 (a,b):
    sum=a+b
    if sum==20 or a==20 or b==20:
        return True
    else:
        return False
    

#print(myfunc2(20,9))
#print(myfunc2(11,9))
#print(myfunc2(12,12))
