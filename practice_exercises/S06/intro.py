class Seq:
    pass

s1 = Seq() #qhen we are creating a class we are defining a new type of data like int, bool, etc
#s1 is an object of type Seq()
#if we dont define an init function, then, we will have an empty class

class Animal:
    def __init__(self, stranimal): #the first parameter must be always the self variable
        self.name = stranimal

    def method_name(self, parameter):
        pass
    def __str__(self):
        #method called when the object is being printed
        return self.stranimal
    #calling a method is like: s1.len(the parameters needed except for the self parameter)

class ParentClass:
    #global class
    pass
class ChildClass(ParentClass):
    #specific class inside the general one
    pass

#now in our example:
class Mammals(Animal):
    def __init__(self, stranimal, pulmonary_sistem=""):
        super().__init__(stranimal)
        self.pulmonary_sistem = pulmonary_sistem