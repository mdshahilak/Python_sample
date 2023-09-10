class First:
    def display(self):
        print("First")
class Second(First):
    def display(self):
        print("second")
class Third(Second,First):
    def display_third(self):
        print("Third")

x=Third()
x.display_third()
x.display()
print(Third.mro())