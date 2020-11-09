import math
# CHECK IF A PRIME NUMBER
    #

def is_prime(n):

    # We know numbers less than 2 are not prime
    if n < 2:
        return False

    # Checking factors up to sqrt(n)
    # for i in range(2, n):
    for i in range(2, int(math.sqrt(n)) + 1): # mathematical optimization...

        # If i is a factor, return false
        if n % i == 0: # i=factor
            return False    # if remainder == 0, it IS a factor (not prime)

    # If no factors were found, return true
    return True # PRIME! (no factors besides 1 and itself)
