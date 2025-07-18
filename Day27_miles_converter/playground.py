# *args unlimited positional arguments. *args is a tuple
def add(*args):
    sum = 0
    for n in args:
        sum +=n
    return sum

print(add(1,2,3,4))

# **kwargs optional keyword arguments. **kwargs is a dictionary

def calculator(n,**kwargs):
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)

    n+= kwargs['add']
    n*= kwargs['multiply']
    print(n)

calculator(2,add=3, multiply=5)