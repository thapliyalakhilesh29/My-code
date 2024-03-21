#Type-1 -- reverse the string
from shlex import join


def reverse1(str):
    newStr = str[::-1]
    return newStr

print(reverse1("hi this is akhilesh"))
#output- hselihka si siht ih


#Type-2 -- reverse the string

def reverse2(str):
    tempStr = str.split()
    temp1 = tempStr[::-1]
    print((temp1))
    temp= join(temp1)
    return temp

print(reverse2("hi this is akhilesh"))
#output- akhilesh is this hi


#Type-3 -- reverse the string

def reverse3(str):
    tempStr = str.split()
    temp1 = tempStr[::-1]
    print((temp1))
    temp= ''.join(temp1)    
    # what u write inside the quote the elemnt will be concat with that thing
    return temp

print(reverse3("hi this is akhilesh"))
#output- akhileshisthishi