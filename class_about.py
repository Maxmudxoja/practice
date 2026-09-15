'''Class

1->What is class
2->ordinary vs static properties
3->special methods

'''

print("=========== What is class =================")

#class->is a reusable blueprint or template used to create objects
#structure-> state, consturctor ,method


class Person():
    #state
    message="class state property"

    #constructor
    def __init__(self, name, age):
         self.name=name
         self.age=age





#method
    def introduce(self):
        print(f" the  {self.name} says: How do you do ?")


    def say_age(self):
         print(f" {self.name} says  I am {self.age}")

    @classmethod
    def explain():
         print("Static method property is executed")




person1 =Person("Justin",25)
person2=Person("Ethan",21)
person3=Person("John",22)

#ordinary state property

print("person1.name: ",person1.name)

#ordinary methods 

person1.introduce()
person2.say_age()


print("=========== ordinary vs static properties =================")

new_message=Person.message
print("new_message: ", new_message)

#static method
Person.explain