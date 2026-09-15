print("========= Number ===========")

# in Java -> variable: name of storage location
# in Python ->variable is named reference !

count= 100
coun_type=type(count)
print("count: ",count, "  Type of the count: ",coun_type)
print(f"the count: {count} and type: {coun_type}")

result1= count.bit_count() # method
result2=count.numerator # state

print(result1, result2)


print("========= String ===========")

# Methods: upper(), lower(), title(),find(), replace()
course= "AI Python FullStack"
result=type(course)
print(f"the result (1): {result}")

result=course.title() # method
print(f"the result (2): {result}")

result=course.upper()
print(f"the result (3): {result}")

result=course.replace("FullStack" ,"MasterClass")
print(f"the result (4): {result}")

print("========= Boolean ===========")

#functions -> type() , input() bool() int() str()

y=input("Give your value for y: ")
print("Value of the y: ", y)

result=y.isnumeric()
print(f"the input value is numeric: {result}")

# Truthy vs Falsy value
# Truthy-> True , 100, -100 "MIT"
# Falsy ->False ,0 ,"",None -> False qiymatlar degani

test_falsy="" or False or None or 0
print("The Falsy: ",bool(test_falsy))

test_truthy=True or 100 or -100 or "MIT"
print("The Truthy: ",bool(test_truthy))