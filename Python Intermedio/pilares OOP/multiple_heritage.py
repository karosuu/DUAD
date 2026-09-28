class Flyable:
    def fly(self):
        return "I can fly"
    
    
class  Swimmable():
    def swim(self):
        return "I can swim"
    
class Duck(Flyable, Swimmable):
    pass

duck = Duck()

print(duck.fly())
print(duck.swim())