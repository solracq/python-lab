'''
@author: Solrac
'''
import Dog

def testDog(name, age):
    #name= input("what is the dog's name: ")
    #age= int(input("what is the dog's age: "))
    
    my_dog = Dog.Dog(name, age)
    
    print("my dog's name is ", my_dog.name.title())
    print("my dog's age is ", my_dog.age)
    
    my_dog.sit()
    my_dog.roll()

testDog("Betoveen", 5)
testDog("Fluffy", 7)