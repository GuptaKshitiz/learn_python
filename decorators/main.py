################################################################
# Code samples from Video
################################################################

# Core Methodology of decorators

def user_name(name="Alice"):
    return name

def greet_name(func):
    print(f"Hi {func()}")

greet_name(user_name)
#----------------------------------------------------------------
# Blueprint of decorators
def test_decorator(func):
    def func_wrapper():
        print("before func")
        func()
        print("after func")
    return func_wrapper

def a_function_requiring_decoration():
    print("need a decorator")

a_function_requiring_decoration()
#outputs: "I am the function which needs some decoration to remove my foul smell"

a_function_requiring_decoration = test_decorator(a_function_requiring_decoration)
#now a_function_requiring_decoration is wrapped by wrapTheFunction()

a_function_requiring_decoration()

#-------------------------------------------------------------------
# How to call a decorators

def test_decorator(func):
    def func_wrapper():
        print("before func")
        func()
        print("after func")
    return func_wrapper

#the @test_decorator is just a short way of saying:
@test_decorator
def a_function_requiring_decoration():
    print("need a decorator")

a_function_requiring_decoration()

#------------------------------------------------------------------
# Nested decorator

from functools import wraps

def test_decorator(func):
    # @wraps helps to prevent overrode the docstring and name of function
    @wraps(func)
    def wrapTheFunction():
        print("before func")
        func()
        print("after func")
    return wrapTheFunction

@test_decorator
def a_function_requiring_decoration():
    print("need a decorator")

print(a_function_requiring_decoration.__name__)
#------------------------------------------------------------------
# Multiple decorators

def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

def exclamation_decorator(func):
    def wrapper():
        result = func()
        return result + "!"
    return wrapper

@exclamation_decorator
@uppercase_decorator
def greet():
    return "hello"
