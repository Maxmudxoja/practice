''' Functions

1-> Define vs Call
2-> Prametr and Argument
3-> Keyword & default argument
4-> Scope 

'''

print("========== Define(parametr) Vs Call (argument) ============")
# buld in functions: print() , type()
# Functions -> resuable block of code 
# In Java, C languages use '{}' as code block | in Pyhton uses indentation !

#Define -building part - Parametr
def greet(a): 
    #pass # def bosh qolmasligi kerak , agar hech narsa yoq bolsa "pass" qoyib ketiladi
    print(f"How do you do : {a}")


def greeting(b):
    print("Greeting is executed")
    return f"Hi: {b}"

#Call -execute- Argument
result1= greet("Ethan")
print("Result1: ",result1)

result2= greeting("Justin")
print("Result2: ",result2)


print("========== Keyword & default argument ============")

#Define 

def give_greet(name, age=22):
    print("give_greet is executed")
    return f"Hi {name}, You are {age} years old!"




#Call -> Keyword argument lar -> yana code ni aniqroq tushunilishi uchun
result3= give_greet(name="Justin", age=20)
print("Result3: ",result3)

#Call -> Default argument
result4= give_greet(name="John")
print("Result4: ",result4)