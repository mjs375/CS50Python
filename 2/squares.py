# How to call the module (another file that defines the function) used here?
from functions import square
# from your file FUNCTIONS(.py), import the particular SQUARE f(x)

# It is useful to put your functions in a whole other file, to clean up and organize your code

"""
import functions #import the whole module
    #if you import this way, down below you would need to call {functions.square(i)}
"""

# import Python built-in functions, pre-written...

#################################################


for i in range(10):
    print(f"The square of {i} is {square(i)}.") #format string!
        #square(i) calls the square() function, using 'i' as the input (substitutes the 'x')
