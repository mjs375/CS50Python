from prime import is_prime

def test_prime(n, expected):
    if is_prime(n) != expected: #call is_prime f(x): is it equal to expected number?
        print(f"Error on is_prime({n}), expected {expected}.")
        #print(f"ERROR on is_prime({n}), expected {expected}")
        # Above prints if NOT correct: a bug found!
