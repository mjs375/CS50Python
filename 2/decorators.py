# F U N C T I O N A L   P R O G R A M M I N G   P A R A D I G M :


# a DECORATOR takes a function as input
    # and outputs a modified function.
    # In Python, a function can takes a function as a value

def announce(f):    #takes as input function f() and outputs [DECORATOR]
    def wrapper(): #simply defining the function
        print("About to run the function.")
        f()
        print("Done with the function.")
    return wrapper #actually does wrapper()!

@announce #adds announce decorator to hello()
def hello():
    print("Hello world")

hello() #actually calling the function
