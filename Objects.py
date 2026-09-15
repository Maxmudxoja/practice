
''' OBJECTS

1->What is object
2->Iterable objects & Range
3->Dictionary
4-> Error handling system

'''

import array # package/module
import math
print("========= What is object ============")
from math import ceil ,asin # specific methodlarni chaqirish

# Object->it is a piece of memory that bundles state (attributes) and behavior (methods) together.
# Object has state and method properties.
# Everything is object in Python!

print(type ('Hello Wrold '))
print(type(100))
print(type(True))
print(type(array))
print(type(math))


# Programming Paradigm->OOP , Funcional programming : style of coding
# OOP 4 concepts-> Abstraction | Encapsulation | Inheritance | Polimorphism
result1=math.ceil(97.7) # call
print(f"Result1:  {result1}")