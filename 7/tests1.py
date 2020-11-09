# Import the unittest library and our function
import unittest
from prime import is_prime # our own function, imported

# A class containing all of our tests
class Tests(unittest.TestCase):

    def test_1(self):
        """Check that 1 is not prime."""
        #doc-string above: describes f(x). Unittest prints out that docstring as a description when fails
        self.assertFalse(is_prime(1))
        #assertFalse : built-in function. is_prime(1) should be False

    def test_2(self):
        """Check that 2 is prime."""
        self.assertTrue(is_prime(2))
        # is_prime(2) should be True

    def test_8(self):
        """Check that 8 is not prime."""
        self.assertFalse(is_prime(8))

    def test_11(self):
        """Check that 11 is prime."""
        self.assertTrue(is_prime(11))

    def test_25(self):
        """Check that 25 is not prime."""
        self.assertFalse(is_prime(25))

    def test_28(self):
        """Check that 28 is not prime."""
        self.assertFalse(is_prime(28))


# Run each of the testing functions
if __name__ == "__main__":
    unittest.main() #run programs
