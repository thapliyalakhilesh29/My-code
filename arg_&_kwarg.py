import math
def myfunc(*arg):
   l= len(arg)
   ans=1
   for i in arg:
      ans=ans*i
   return ans
      
   
    

result= myfunc(2,4,2)
print(result)



