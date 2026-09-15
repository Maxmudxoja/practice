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