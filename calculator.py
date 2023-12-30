def calculator(num1, num2):
    sum=num1+num2
    multiplication= num1*num2
    division= num1/num2
    subtraction= num1-num2
    return sum , multiplication , division , subtraction


a =int(input("Enter first number: "))
b =int(input("Enter second number: "))
result= calculator(a,b)
print('Entet 1 for summation, Entet 2 for Subtraction,Entet 3 for Multiplication,Entet 4 for Division  ')
operation= int(input("Enter the valid opertaion: "))
if operation==1:
    print(f'the summation of two number is : {result[0]}')
elif operation==2:
    print(f'the Subtraction of two number is : {result[3]}')
elif operation==3:
    print(f'the Multiplication of two number is : {result[1]}')
elif operation==4:
    print(f'the Division of two number is : {result[2]:.2f}')
else :
    print("Invalid Input")

