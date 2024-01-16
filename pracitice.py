# this how to call fuction from other file/ directory
# from "package_name" import "module_name/file_name"
# from "file_name" import "function_name"
# from "folder_name.subfolder_name.file_name" import "function_name"
# NOTE- make sure each folder and subfolder must contain a .py file name "__init__.py" so that pyhon would know that that folder/subfolder is module of a python package


from package1 import module1

result = module1.myfunc2(20,9)
print(result)




from function_problem1 import myfunc

print(myfunc(8,9))



