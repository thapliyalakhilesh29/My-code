def myfunc(string):
    modified_string = ""
    for i in range(len(string)):
        if i % 2 == 0:
            modified_string += string[i].upper()
        else:
            modified_string += string[i].lower()
    return modified_string

# result = myfunc('akhilesh')
# print(result)


def myfunc2 (a,b):
    sum=a+b
    if sum==20 or a==20 or b==20:
        return True
    else:
        return False
    

#print(myfunc2(20,9))
#print(myfunc2(11,9))
#print(myfunc2(12,12))


