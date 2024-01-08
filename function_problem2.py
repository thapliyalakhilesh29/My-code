'''def myfunc1(a):
    if a in range(90, 111) or a in range(190, 211):
        return True
    else:
        return False


print(myfunc1(int(89.5)))'''


'''def myfunc2(list):
    l=len(list)
    for i in range(1,l):
        if list[i-1]==3 and list[i]==3:
            return True
    return False

    
       
    
print(myfunc2([3,3,4,3,9,7]))
print(myfunc2([2,4,3,3]))
print(myfunc2([2,4,3,0,3]))
print(myfunc2([2,4,3,3,5,4]))'''


'''
def myfunc3(*arg):
    my_num = list(arg)
    result =[]
    for num in my_num:
        result.append(num**2)
    return result


print(myfunc3(1,2,3,4,5,6,7,8,9,10))

'''

l1= ['a','b','c']
l2= ''.join(l1)
print(l2)   



