#Dunder-> buning ma'nosi double underscore degani (__) (Pythonni ichki qurulish mexanizmi , ya'ni methodlar va boshqalar)
#-> __builtins__ , __init__

message="In Python everything is object"
print(message)

result=type(message)
print("Result: ", result)


"""
In Python , there are builtin tools:
1-> Types: int , float, str, list, dict
2->Function: print(), len(),input(), type(), str() , int()
3-> Constants : True,False,None
"""

print(dir(__builtins__))