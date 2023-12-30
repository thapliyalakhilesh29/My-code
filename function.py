def puzzle (input):
    if input%3==0 and input%5==0:
        return "fizzbuzz"
    elif input%3==0:
        return "fizz"
    elif input%5==0:
        return "buzz"
    else:
        return input
    

output= puzzle(45)
print(output)
