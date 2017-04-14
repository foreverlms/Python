class Animal(object) :
    def __init__(self,kind):
        self.kind=kind
    def __init__(self):
        self.kind='Animal'
    def run(self):
        print('Animal is running ...')
class Dog(Animal) :
    def __init__(self,kind,subkind):
        super()
        self.subkind=subkind
    def run(self):
        print('%s is running ...' %self.subkind)
class Cat(Animal) :
    pass
a=Animal()
a.run()
dog=Dog('animal','Dog')
cat=Cat()
dog.run()
cat.run()
print(type(a))
print(type(dog))
print(type(dog))
print(dir(object))