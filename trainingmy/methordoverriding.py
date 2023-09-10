class BaseClass:
    def __init__(self):
        print("Base init")
        
    def set_name(self,name):
        
        self.name=name
        print("base set")

    
    
class SubClass(BaseClass):
    def __init__(self):
        print("sub init")
    def welcome(self):
        print("Welcome")
    def display_name(self):
       print("Name:"+self.name) 
        
    def set_name(self,name):
        
        self.name=name 
        print("sub set")



y=SubClass()

y.set_name("Shiju")

y.welcome()
y.display_name()

