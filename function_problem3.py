def volume(r):
    # volume of sphere
    return (4/3)* (22/7)*r**3
    
result= volume(2)
print(f'Volume of sphere is {result}')




def func1(num,UL,LL):
    # find out the the num is in range of the given numbers i.e. UL & LL
    
    if num >=LL and num <=UL:
        return True
    else:
        return False


print(func1(num=21,LL=10,UL=90))



def func2(num,UL,LL):
    # Another method to find out the the num is in range of the given numbers i.e. UL & LL
    return num in range(LL, UL+1)

print(func2(num=9, LL=10,UL=30))



def func3(my_list):
    #print a list which consists only unique item from given list
    result=set(my_list)
    return list(result)


print(func3([1,1,1,13,3,35,5,6,6,6]))



def multiply(list1):
    #print the multiplication of all items of a given list
    result=1
    for i in list1:
        result *=i
    return result

print(multiply([2,3,4,5]))


def func4(string1):
    #check whether the given string is palindrome or not
    # first we have to replace spaces from the string & also make it case independent
    # then reverse the string and compare it with original one
    s= string1.replace(' ','').upper()
    if s == s[::-1]:
        return True
    else:
        return False
    
print(func4('hoH'))




    

