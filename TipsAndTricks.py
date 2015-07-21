import sys
import time

print("""
Tips and Tricks in Python
-------------------------
This is a tutorial which goes over many small and "hidden" features in
python that are useful to know and use, but otherwise would not be known.
""")

stop = input('Press [Enter] to continue...')
print('\n'*100)

print("""
###
## Quotation Marks
###

Python has four types of quotation marks. Firstly, there are the single and
double quotation marks ' and ". Both are valid for enclosing strings. The
utility of these is that if one is used to enclose a string, the other can be
used as part of that string. I.e., one can write

str1 = "I can't carry all these lemons!"
str2 = 'He said, "Can I have some lemons?"'

There are also triple single quotes and triple double quotes, ''' and """+
'''"""
respectively. Any text inside these quotes maintains its exact formatting,
newlines and all.
''')

stop = input('Press [Enter] to continue...')
print('\n'*100)

print("""
###
## Integer Division
###

In python 3 (this does not apply to python 2 and lower), any division is
automatically processed as floating point division, even if both components
are integers. This means we get the following results

>>>1/2
0.5
>>>1./2.
0.5

If we want to explicitely do integer divison, we can use the // operator as such

>>>1//2
0
>>>1.//2.
0.0
""")

stop = input('Press [Enter] to continue...')
print('\n'*100)

print("""
###
## String Concatenation
###

Python supports the ability to add strings together via the '+' operator.
However, since strings are immutable, this is wildly innefficient if you are
constantly changing strings. Every time two new strings are added together,
an entirely new memory space must be allocated for this new string, rather
than appending to the current memory space of one of the strings. To overcome
this, python has a nice feature. Consider that you have the strings

food1 = 'milk'
food2 = 'eggs'
food3 = 'spam'

You could create a new string by the following

grocery_list = food1 + ', ' + food2 + ', ' food3

which would result in grocery_list being 'milk, eggs, spam'. Rather than
adding each string together however, you can concatenate them much more
efficiently by doing the following.

grocery_list = '%(food1)s, %(food2)s, %(food3)s' % (food1, food2, food3)

This process will see the %, known as the interpolation operatorand attempt
to insert a variable there based on the proceeding variable name in
parentheses. The s after this indicates the variable is a string (you can use
i for ints, f for floats, etc.) This will then substitute the food1 variable
into that component of the string, and do similar procedures for the rest of
the string. An even more convenient way to do this is to use the locals()
dict. This is a dict that exists in every instance of a pythin runtime event
that stores all local variables. Thus the following is viable.

grocery_list = '%(food1)s, %(food2)s, %(food3)s' % locals()
""")

stop = input('Press [Enter] to continue...')
print('\n'*100)

print("""
###
## Chaining Comparison Operators
###

In most languages, you would have to do the following.

if (5 < x and x < 10):
    Do Something

In python, you can chain the comparisons as below.

if (5 < x < 10):
    Do Something
""")

stop = input('Press [Enter] to continue...')
print('\n'*100)

print("""
###
## Get Last Answer
###

In the command line for python, you can get the last returned value with the
_ character.

>>> 5*5
25
>>> x = _
>>> print(x)
25
""")

stop = input('Press [Enter] to continue...')
print('\n'*100)

print("""
###
## For Else Statements
###

For loops can have an associated else statement that is executed if the for
loop runs to completion.

for i in range(10):
    if (i == 10):
        break
else:
    print("For Loop Ran To Completion")

In this case, since i is never equal to 10 (remember range goes from 0 to 9)
the break was never reached and the for loop ran through all its elements.
This is a good way to simply check that a for loop completed.
""")

stop = input('Press [Enter] to continue...')
print('\n'*100)

print("""
###
## Value Swapping
###

One task that is often necessay in coding is to switch the value of two
parameters, such as a and b. The standard proecdure is to do

c = a
a = b
b = c

In python, you can swap in place with a single line

a, b = b, a
""")

stop = input('Press [Enter] to continue...')
print('\n'*100)

print("""
###
## Ternary Operator
###

Most languages have something known as the ternary operator which takes the
form

x = (conditional ? if_true : if_false)

where the value returned is the first one if the conditional statement is true
and the second one if the conditional statement is false. Python has a similar
format which mimics this operator.

x = if_true if conditional else if_false
""")

stop = input('Press [Enter] to continue...')
print('\n'*100)

print("""
###
## Boolean Math
###

Booleans and conditional statements can be used in mathematical expressions.
Anything which is true converts to a 1 and anything which is false converts
to a 0. The following is valid

>>> x = 5
>>> print(5*(x < 10))
5
>>> print(5*(x > 10))
0
""")

stop = input('Press [Enter] to continue...')
print('\n'*100)

print("""
###
## Ellipses Operator
###

There exists an Ellipsis operator ... which is useful when dealing with very
large dimensional arrays. We can create a 4D 2x2x2x2 array.

>>> arr = np.arange(16).reshape(2,2,2,2)
>>> arr[...,0].flatten()
array([ 0,  2,  4,  6,  8, 10, 12, 14])

The ... operator in this case gives us all of the first three dimensions, and
we specifically request the first component of the last dimension. This
process is equivalent to

>>> arr[:,:,:,0].flatten()
array([ 0,  2,  4,  6,  8, 10, 12, 14])
""")

stop = input('Press [Enter] to continue...')
print('\n'*100)

print("""
###
## is vs. ==
###

Python has two comparison features. One is == and the other is the keyword is.
The first, ==, compares by value. The second, is, compares by reference. When
comparing to True, False, None, etc, use is.

These two comparison operators can become somewhat dangerous when comparing
numbers. For efficiency reasons, python stores all integers from -5 to 256
in memory. When you say x = 10, x is a reference to the already stored 10
in memory. Thus we find that

>>> x == 10
True
>>> x is 10
True

BUT... if x = 1000, we see that

>>> x == 1000
True
>>> x is 1000
False

Note, the last comparison checked if the reference for x was the same as the
reference for 1000, but there is no referece for 1000! Moral of the story,
always make sure to use == or is, as appropriate.
""")

stop = input('Press [Enter] to continue...')
print('\n'*100)

print("""
###
## Chaining conditionals with and
###

When considering an if statement of multiple conditionals, all connected by
and, such as the following

if (condition1 and condition2 and condition3 and ...):

python will only check the veracity until it reaches a False, at which point
it stops checking. This means if a conditional is a function, it may not
execute. Consider the following

def func():
    print('Function Called!')
    return true

if (10 > 5 and abs(-1) == 1 and func()):
    print('If statement is true!')

The ouput of this if statement is

Function Called!
If statement is true!

Now consider this if statement

if (10 > 5 and abs(-1) == 2 and func()):
    print('If statement is true!')

The output is nothing! Since abs(-1) != 2, python stops checking the conditions
and func() is never called. Likewise the print inside the if is also never
called. This feature is useful if we only want the function to execute under
certain conditions.
""")

stop = input('Press [Enter] to finish...')
print('\n'*100)
print('Done...')
