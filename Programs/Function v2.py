import pdb

print("""
Short Tutorial on Functions - part II
-------------------------------------
This tutorial is a continuation of the "Short Tutorial on Functions - part I".
It will cover some slightly more advanced features of functions in python.
After each new topic is displayed, the program will enter the python debugger,
pdb, which will allow you to play with the functions defined for each component
and test them out. When you are finished and want to move on, just type
continue. Remeber you can check a function's docstring by typing
help( func_name ). Let's jump right into it.
""")

stop = input('Press [Enter] to continue...')
print('\n'*100)

print("""
###
## args
###

In the last tutorial, the topic of input parameters to a function was
discussed. One can do something similar to the following

def line(m, x, b):
    return m*x + b

where the function explicitely requires that m, x, and b be passed into the
function for it to be called properly. However, what if you don't know how many
arguments you want to accept? You can account for this with the *args parameter
as an input parameter. Note that the important component of this is the *
symbol this signifies any arguments passed into the function which are beyond
the standard required inputs go into this variable. The variable name is
usually arg by convention, but can be anything you choose. The following
function makes use of this possible input parameter

def printArgs1(*args):
    for i, arg in enumerate(args):
        print('Argument', i, 'is equal to', arg)

You could have also defined two required inputs, plus a set of *args. The
following is valid

def printArgs2(a, b, *args):
    print('Sum of first two arguments is', a+b)
    for i, arg in enumerate(args):
        print('Argument', i, 'is equal to', arg)

You could have defined something like printArgs3(a, *args, b), but the user
would have had to specifically state which value was b by calling
printArgs3(1, 2, 3, 4, 5, b = 6) In which case a = 1, args = (2, 3, 4, 5) and
b = 6. This is not common practice and should be avoided.
""")

def printArgs1(*args):
    """
    A function to print out all input arguments, including their position in
    the args array and their value.
    
    Args:
        args   - The optional arguments which get printed out
        
    Returns:
        Nothing
    """
    for i, arg in enumerate(args):
        print('Argument', i, 'is equal to', arg)

def printArgs2(a, b, *args):
    """
    A more complicated function than printArgs1 because this takes in two
    required arguments, a and b, the sum of which is printed out. Then the
    same procedure is applied as before where all the *args are printed.
    
    Args:
        a      - The first argument
        b      - The second argument, should be additive to a
        args   - The optional arguments which get printed out
        
    Returns:
        Nothing
    """
    print('Sum of first two arguments is', a+b)
    for i, arg in enumerate(args):
        print('Argument', i, 'is equal to', arg)

pdb.set_trace()
print('\n'*100)

print("""
###
## kwargs
###

Aside from allowing unlimited extra parameters, python also allows unlimited
extra parameters which have names associated with them. If you remember your
python collections, this should sound exactly like a dict, and thats exactly
what this is. Just as with args, there is the special character ** that must
precede your kwargs name to designate that it will act as a kwargs parameter.
Note that just as with args, the name kwargs is arbitrary, but chosen to be
kwargs by convention. Thus, you can define a function such as the following.

def printKwargs(**kwargs):
    for kwrd, value in kwargs.items():
        print('Keyword Argument', kwrd, 'is equal to', value)

You of course have the complete freedom to include both args and kwargs as
inputs along with required arguments and keyword arguments. Note that the
order of *args and **kwargs doesn't matter, but both should be after all
required inputs. The following is a valid function.

def printAll(a, x, b = 0, *args, **kwargs):
    print('y = a*x + b =', a*x+b)
    for i, arg in enumerate(args):
        print('Argument', i, 'is equal to', arg)
    for kwrd, value in kwargs.items():
        print('Keyword Argument', kwrd, 'is equal to', value)
""")

def printKwargs(**kwargs):
    """
    A function to print out all input kwarg parameters including their
    associated name and value.
    
    Args:
        kwargs - The optional keyword arguments which get printed out
        
    Returns:
        Nothing
    """
    for kwrd, value in kwargs.items():
        print('Keyword Argument', kwrd, 'is equal to', value)

def printAll(m, x, b = 0, *args, **kwargs):
    """
    A function to calculate y = m*x + b, and print out the rest of the
    input args and kwargs.
    
    Args:
        m      - The slope
        x      - The x value
        b      - The y intercept, zero by default
        args   - The optional arguments which get printed out
        kwargs - The optional keyword arguments which get printed out
        
    Returns:
        Nothing
    """
    print('y = m*x + b =', m*x+b)
    for i, arg in enumerate(args):
        print('Argument', i, 'is equal to', arg)
    for kwrd, value in kwargs.items():
        print('Keyword Argument', kwrd, 'is equal to', value)

pdb.set_trace()
print('\n'*100)

print("""
###
## Default Parameters Part I
###

You can assign default values to input parameters for functions, such that if
it is not explicitely defined by the user, the default value is used. However,
there is a cautionary tale that must be considered as in the function below.

def addOneBad(data = []):
    data.append(1)
    return data

You might expect that if one calls addOne(), with no arguments, that the
argument data is instatiated as an empty list, the value 1 is added to it,
and the list is returned. However, let's try calling it several times.

>>> addOne()
[1]
>>> addOne()
[1, 1]
>>> addOne()
[1, 1, 1]

Clearly the method is adding 1 to the running list that is being kept between
calls. The reason for this is that data = [] is only initialized on the very
first function call. Every time after, data is pointing to the list associated
with the function that still held the values from last time the function was
called. This means the function continually adds to the same list since the
object data never points to a new empty list. This function is defined so you
can test it out for yourself.
""")

def addOneBad(data = []):
    """
    Simply returns the input data with one appended to the end. If no list
    is input, one is appended to an empty list.
    
    Args:
        data - A list to append the value one to. Default is an empty list
        
    Returns:
        A list with one appended to the end. This class is a cautionary tale
        about using default values which are mutable.
    """
    data.append(1)
    return data

pdb.set_trace()
print('\n'*100)

print("""
###
## Default Parameters Part II
###

A more proper way of accomplishing the task in part I is to do the following.

def addOneGood(data = None):
    if (data is None):
        data = []
    data.append(1)
    return data

Try out this function to make sure that it works as you'd expect.
""")

def addOneGood(data = None):
    """
    Simply returns the input data with one appended to the end. If not list
    is input, one is appended to an empty list.
    
    Args:
        data - A list to append the value one to. Default is an empty list
        
    Returns:
        A list with one appended to the end. This class properly appends to
        an empty list without the issues seen in the addOneBad function.
    """
    if (data is None):
        data = []
    data.append(1)
    return data

pdb.set_trace()
print('\n'*100)

print("""
###
## Nested Functions Part I
###

In python, functions are known as "first-class" objects. This means they act
and can be treated exactly like a real object of a class. You may not entirely
know what this means right now, but over time this knowledge will take on a
greater meaning. For now, just know that the fact that functions are
"first-class" means they can have nested functions inside them. An example is
as follows.

def outer(n):
    def inner(x):
        return x ** n
    return inner

This is a function which defines a function inside it. The outer function takes
the argument n, which becomes the exponent of the inner function. The inner
function takes the argument x which is raised to the n and squared. This
function can be used as follows.

>>> f = outer(2)
>>> g = outer(3)
>>> f(2)
4
>>> f(3)
9
>>> g(3)
27

Both f and g are the inner function. Note how both f and g retain their
knowledge of n which is a part of the inner function, even though it was passed
into the outer function.
""")

def outer(n):
    """
    This function returns a function that raises the input to the power n.
    
    Args:
        n - The exponent to be used in the returned function
        
    Returns:
        A function that raises the input to the power of n
    """
    def inner(x):
        return x ** n
    return inner

pdb.set_trace()
print('\n'*100)

print("""
###
## Nested Functions Part II
###

The previously defined nested function utilizes the concept of closure. You may
feel unnerved by the fact that inner is capable of remembering the value of n.
The reason it is able to do this is because of closure. Effectively the inner
function is a member of the outer function, just as the variable n is. When
we say f = outer(2), we are setting f to a saved state of the inner function
in which it has access to the inner function and the associated value of n,
which the inner function "closes over". In effect, closure is just a fancy
name for a function that remembers the values from the enclosing scope even
when the program flow is no longer in the enclosing scope.
""")

pdb.set_trace()
print('\n'*100)

print("""
###
## Decorators Part I
###

Decorators offer a powerful way to change the functionality of a function
without having to modify the code inside that function. This topic is somewhat
advanced, but hopefully this basic rundown at least puts the idea in your
head for when you need it later, when you can look it up in more detail. The
topic of decorators is particularly powerful for OOP. To start, let's consider
the nested function and second function below.

def decorator(func):
    def inner(a):
        return func() + a
    return inner

This is similar to the nested function above, except now the inner function has
knowledge of the passed in function called func. The inner function calls the
function func() that was passed into the outer function, and adds the value
a to it, effectively modifying the functionality of the passed in function.
We say that inner "decorates" the function with new features. Let's define a
function to use then.

def one():
    return 1
""")

def decorator(func):
    """
    Used to decorate a function to allow for adding a value to the function.
    """
    def inner(a):
        return func() + a
    return inner

def one():
    """
    Function to return the value 1
    """
    return 1

stop = input('Press [Enter] to continue...')
print('\n'*100)

print("""
###
## Decorators Part II
###

We can see that one() just returns 1. But we can do the following

>>> one()
1
>>> one = decorator(one)
>>> one(2)
3
>>> one()
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    one()
TypeError: inner() missing 1 required positional argument: 'a'

Note how when we redefined one using the decorator function, it attained a new
functionality that required an input into the function. It can no longer act
like just one(). We could have instead defined addOne = decorator(one), which
would have left the fuction one as it was. Note that this program includes
a function called resetOne which can be called to reset the original state of
one by the following one = resetOne().
""")

def resetOne():
    def one():
        return 1
    return one

pdb.set_trace()
print('\n'*100)

print("""
###
## Decorators Part III
###

In truth, the simple example shown here does not fully convey the power and
utility of decorators. They offer a much broader scope of functionality when
you start dealing with OOP and classes. For now though, it is useful to under-
stand their functionality and keep it in the back of your mind that they exist
and can be used. There is one small feature which is worth mentioning that will
be important once you begin OOP. When defining a function, you can explicitely
tell python that it will be decorated by another function with the @ symbol.
Using the above example, where we wrapped the one function with the decorator
function, you might define the one function as follows.

@decorator
def one:
    return 1

This tells python to automatically decorate the function one with the function
decorator right from the getgo so that the user never sees the functionality of
one().
""")

stop = input('Press [Enter] to continue...')
print('\n'*100)
print('Done...')
