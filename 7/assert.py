# T E S T I N G _ P R A C T I C E S

def square(x):
    return x * x

assert square(10) == 100 # if False, log to console & STOP
# When assert runs, and expression is TRUE, it ignores itself
    # When FALSE, assert gives an 'AssertionError' in the console.

# # More Basic Testing practice:
#print(square(10)) # print answer
#print(square(10) == 100) # print correct or not


""" Output:
Traceback (most recent call last):
  File "square.py", line 6, in <module>
    assert square(10) == 100

AssertionError
"""
