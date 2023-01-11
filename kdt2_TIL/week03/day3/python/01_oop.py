class Person:
    
    def greetinmg(self):
        return 'hi....'
    
iu = Person()
jimin = Person()

print(type(iu))
print(type(jimin))
print(type([1, 2, 3]))
print(type([]))

iu.name = '아이유'
jimin.name = 'BTS 지민'

print(iu.name)
print(jimin.name)
print(type(iu.name))

print('apple banana'.split()[0].upper().strip()[2])