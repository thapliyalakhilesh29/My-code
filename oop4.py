import math;

def solution (a,b):
    c=[]
    
    i = len(a)-1; # start adding from end
    j = len(b)-1;
    carry = 0;
  
    while(i >=0 and j >= 0):
        sumVal = a[i] + b[j] + carry 

        if(sumVal > 9):
            # store carry e.g. 23 -> 2
            carry = math.floor(sumVal/10);
            # store last value e.g. 23 -> 3
            c.append(sumVal%10);
        else:
            # store value
            c.append(sumVal);
            # reset carry
            carry = 0;
        i-=1;
        j-=1;
        
    while(i >=0):
        sumVal = a[i] + carry 

        if(sumVal > 9):
            # store carry e.g. 23 -> 2
            carry = math.floor(sumVal/10);
            # store last value e.g. 23 -> 3
            c.append(sumVal%10);
        else:
            # store value
            c.append(sumVal);
            # reset carry
            carry = 0;
        i-=1;

    while(j >= 0):
        sumVal = b[j] + carry 

        if(sumVal > 9):
            # store carry e.g. 23 -> 2
            carry = math.floor(sumVal/10);
            # store last value e.g. 23 -> 3
            c.append(sumVal%10);
        else:
            # store value
            c.append(sumVal);
            # reset carry
            carry = 0;
        j-=1;
        
    while(carry != 0):
        if(carry > 9):
            carry = math.floor(carry/10)
            c.append(carry%10)
        else:
            c.append(carry)
            carry=0
    
    return c

totalSum = solution([1,2,3,4], [3,4,9])
totalSum.reverse()
print(totalSum)