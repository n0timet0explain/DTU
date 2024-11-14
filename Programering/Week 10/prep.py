# n = 15
# print(type(n))

# s = 'Hello'
# print(type(s))

# d = {'a': 1, 'b': 2}
# print(type(d))

# l = [1, 2, 3]
# print(type(l))



# class MyClass:
#     pass

# my_object = MyClass()
# print(type(my_object))
# print(my_object)




# class MyClass:
#     def __init__(self):
#         print('When is this printed? What is self?')

# print('    This is before I create an object')
# my_object = MyClass()
# print('    This is after I create an object')
# print(type(my_object))



# class Person:
#     def __init__(self, name):
#         self.name = name

# a = Person('Anja')
# print(type(a))
# print(a)
# print(a.name)

# b = Person('Birgite')
# print(type(b))
# print(b)
# print(b.name)


class MyClass:
    def __init__(self, height):
        self.height=height


my_object=MyClass(10)
second_box=MyClass(20)
second_box.height=5
print(my_object.height)