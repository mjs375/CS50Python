n = int(input("Number: ")) #Prompt the user for a number
    # input() ALWAYS gives back a 'str'-type.
    # int(argument) CASTS its contents as an integer

if n > 0: #variable, boolean expression
    print("n is positive") #indentation is REQUIRED: what is inside the IF-statement
elif n < 0: #else-if...:
    print("n is negative")
else: # logically, n is negative
    print("n is zero")


# PYTHON EXCEPTION:
# TypeError: '>' is not supported between instances of 'str' and 'int'
#   TypeError: mismatched types! it expected something else...
# Traceback: shows what part of the code is to blame for the problem.
