#Scope means where a variable can be accessed in your code.
#Python follows the LEGB rule to resolve names.
# LEGB Rule (Very Important)
# Python looks for a variable in this order:
# L — Local (inside current function)
# E — Enclosing (outer function, if nested)
# G — Global (module level)
# B — Built-in (Python built-ins like len, print)

username = 'Shahroz'  #Global Scope Acess Every Where

def func():
    username = 'Malik'  #Local variable or Function Scope Access only inside the function
    print(username)


print(username)
func()

x = 99

def func2(y):
    z = x + y  # the value of x will take from global varriable x and y will take as parameter  
    return z

result = func2(1)
print(result)

# def func3():
#     global x  #don't do this. this is a bad practice don't override the global variable
#     x = 12

# func3()
# print(x)


def f1():
    x = 88    #Enclosing Scope (Nested Functions)
    def f2():
        print(x)  #88
    f2()
f1()  

print(len("Python"))  #Built-in Scope

#Clouser
#A closure is a function that remembers variables from its enclosing scope, even after that scope has finished execution.
#OR
# A closure is a function that:
# Is defined inside another function
# Uses variables from the outer function
# Remembers those variables even after the outer function has finished

def f3():
    x = 90
    def f4():
        print(x)  #88
    return f4 # It return full function definition and also all associative varrible
resultf3 = f3()
resultf3()

def coder(num):
    def actual(x):
        return x ** num
    return actual

f = coder(2)
g = coder(3)

# print(f)
print(f(3))
print(g(3))
