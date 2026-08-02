# def greet():
#     print("hello")

# greet()

# def greet(name):
#     print("hello", name)

# greet("Jack")
# greet("Casper")
# greet("Olivia")

# def add(num1, num2):
#     result = num1 + num2
#     print(result)

# add(3, 5)
# add(2.5, 4)

# def greet(name="everyone"):
#     print("hello", name)

# greet("Jack")
# greet()

# def add(num1, num2):
#     result = num1 + num2
#     return result

# x = add(3, 5)
# print(x)

# scope = 8

# def show_scope():
#     print("inside func:", scope)

# show_scope()
# scope = 4
# print("outside func: ", scope)

def show_local():
    a = 4
    print(a)

show_local()
print(a)