def myfunc(string):
    modified_string = ""
    for i in range(len(string)):
        if i % 2 == 0:
            modified_string += string[i].upper()
        else:
            modified_string += string[i].lower()
    return modified_string

result = myfunc('akhilesh')
print(result)
