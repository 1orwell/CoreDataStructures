import sys

def returndec():
    return 'otherdec string'
    

# dec = otherdec(string)
def newfun(string):
    def dec(func):
        def grouping(name_in):
            print("before",string)
            hello_sent = func(name_in)
            print("after")
            return hello_sent
        return grouping
    return dec 

# hello = newfun('mystring')(hello)
@newfun('mystring')
def hello(name):
    print(f"hello there {name}")
    return f'hello {name}'

name = input("Enter name: ")
print(hello(name))