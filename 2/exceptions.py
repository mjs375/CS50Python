import sys # a module to lets you 'escape' a program

try: #if you run into a bug/error, the 'except' code will handle it gracefully (and not crash!)
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: invalid input!")
    sys.exit(1)

try: #TRY to run this, unless...
    result = x / y
except ZeroDivisionError: #then, don't crash/bug out, but do the following:
    print("Error: cannot divide by 0!")
    sys.exit(1) #error code 1 means something went wrong


print(f"{x} / {y} = {result}.")
# if you divide by zero, you get a messy ErrorMessage... you don't want that!
