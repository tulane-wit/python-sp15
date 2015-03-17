# If we want to run the same set of commands over and over, we can combine the commands into a function.
# A function is a series of transformations that turn an input into an output.
# A function is created by using the command 'def', giving the name of the function you're making,
# and then putting the names of whatever variables you want to use as input in parentheses.


# We can give strings, numbers, or Booleans as input,
# or we can just do empty parentheses if the function doesn't need any input.
# Python uses whitespace to indicate where the function's set of commands begins and ends.


def printFunction(s):
    x = "hello "
    z = x + s # the plus sign concatenates two strings
    print z


# remove the pound sign in the next line to run this function on the input string 'programmers!'
#printFunction('programmers!')




# we can also ask a function to return an output instead of just printing it out,
# so we can store it as a value or use it in another function.


def sum(n1, n2):
    return (n1 + n2)
 
 
x = sum(1,2)
#print x
 
# this does the same thing as print sum(1,2)





# If we want the computer to do something for a certain period of time, we can use a loop.
# In python, two of the most common loops are for-loops and while loops.

def printDigits(x):
    i = 0
    while i < x:
        print i
        i = i + 1

#printDigits(3)


# range(x) is the same as an array of the first ten digits: [0,1,2,3,4,5,6,7,8,9]

result = []
for x in range(10):
    result.append(x)

#print result

# if we want the computer to only do something under certain conditions, we can use an if/then conditional statement:

#if 8 % 2 == 0:
#    print "8 is an even number"
#elif 8 % 2 == 1:
#    print "8 is an odd number"
#else:
#    print "something weird must be happening!"
    

print
# this just skips a line when we print to the console in the tab below.


# now we can try putting all of these things together into functions!


# what if we want to print a triangle?


def triangle(x):
    i = 1
    while i <= x:
        print i * "0"
        i = i + 1

triangle(3)


# see what other shapes you can make!