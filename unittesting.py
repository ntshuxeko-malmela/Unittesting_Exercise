import unittest

def get_even_numbers(numbers): # a function takes a list of numbers
    even_numbers = [] # declare an empty list
    
    for number in numbers:
        if number % 2 == 0: # check is the number is even
            even_numbers.append(str(number)) # add to the list of even numbers
            
    return ', '.join(even_numbers) # return a string of even numbers separated by comma


def get_odd_numbers(numbers): # a function takes a list of numbers
    odd_numbers = [] # declare an empty list
    
    for number in numbers:
        if number % 2 != 0: #check if the number is odd
            odd_numbers.append(str(number)) # add to the list of odd numbers
            
    return ', '.join(odd_numbers) # return a string of odd numbers numbers separated by comma

class TestNumberFunctions(unittest.TestCase):

    def test_get_even_numbers(self):
        self.assertEqual(get_even_numbers([0, 1, 2, 3, 4, 5, 6]), '0, 2, 4, 6')
        self.assertEqual(get_even_numbers([1, 3, 5]), '')
        self.assertEqual(get_even_numbers([]), '')
        self.assertEqual(get_even_numbers([10, 15, 20]), '10, 20')

    def test_get_odd_numbers(self):
        self.assertEqual(get_odd_numbers([0, 1, 2, 3, 4, 5, 6]), '1, 3, 5')
        self.assertEqual(get_odd_numbers([2, 4, 6]), '')
        self.assertEqual(get_odd_numbers([]), '')
        self.assertEqual(get_odd_numbers([10, 15, 20]), '15')

if __name__ == '__main__':
    unittest.main()