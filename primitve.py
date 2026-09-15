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

