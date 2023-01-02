class Dog:
    # Class Variable
    attr1 = "mammal"
    attr2 = "dog"
	
    def __init__(self, name = None): # Default name = None if no input value
	 # Instance Variable   
        self.name = name

    def fun(self):
        print("I'm a", self.attr1)
        print("I'm a", self.attr2)
 

Rodger = Dog()
print(Rodger.attr1 == Dog.attr1)  # true
Rodger.fun()