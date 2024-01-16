
'''
Task 1:

Reverse a message so that the words and letters passed into it are made lower case and reversed. In addition, capitalise the first 
letter of the newly reversed words. If a number or symbol(!#,>) is now in the first position of the word, no capitalisation needs to occur.

Example:
reverseMessage('This is an example of a Reversed Message!');
Returns: '!egassem Desrever A Fo Elpmaxe Na Si Siht'
'''

# Solution:
def new_srting(str_new):
    return ' '.join([''.join(list(i.lower())[::-1]).title() if i[-1].isalpha() else ''.join(list(i.lower())[::-1]) for i in str_new.split(' ')][::-1])

'''
Task 2:

Thanks to the effects of El Nino this year my holiday snorkelling trip was akin to being in a washing machine... Not fun at all.

Given a string made up of '~' and '_' representing waves and calm respectively, your job is to check whether a person would become seasick.
Changes from calm to wave or wave to calm will add to the effect (really wave peak to trough but this will do). Find out how many changes in 
level the string has and if that number is more than 20% of the length of the string, return "Throw Up", else return "No Problem".
'''

# Solution:
def sea_sick(sea):
    changes = sum(1 for i in range(len(sea)-1) if sea[i] != sea[i+1])
    return "Throw Up" if changes > len(sea) * 0.2 else "No Problem"

# Tests:
import codewars_test as test
from solution import sea_sick

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(sea_sick("~"), "No Problem")
        test.assert_equals(sea_sick("_~~~~~~~_~__~______~~__~~_~~"), "Throw Up")
        test.assert_equals(sea_sick("______~___~_"), "Throw Up")
        test.assert_equals(sea_sick("____"), "No Problem")
        test.assert_equals(sea_sick("_~~_~____~~~~~~~__~_~"), "Throw Up")


'''
Task 3:

Find the greatest common divisor of two positive integers. The integers can be large, so you need to find a clever solution.
The inputs x and y are always greater or equal to 1, so the greatest common divisor will always be an integer that is also greater or equal to 1.
'''

# Solution:
def mygcd(x, y):
    while y:
        x, y = y, x % y
    return abs(x)

# Tests:
import codewars_test as test
from solution import mygcd

@test.describe("Example tests")
def example_tests():
    
    @test.it("Examples")
    def examples():
        test.assert_equals(mygcd(30, 12),  6)
        test.assert_equals(mygcd(36, 12), 12)
        test.assert_equals(mygcd( 8,  9),  1)
        test.assert_equals(mygcd( 1,  1), 1)


'''
Task 4:

Write a function that can return the smallest value of an array or the index of that value. The function's 2nd parameter 
will tell whether it should return the value or the index.
'''

# Solution:
def find_smallest(numbers, to_return):
    if to_return == 'value':
        return min(numbers) 
    elif to_return == 'index':
        return numbers.index(min(numbers))
    else:
        return 0
    
# Tests:
import codewars_test as test
from solution import find_smallest

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(find_smallest([5,4,3,2,1],"value"),1)
        test.assert_equals(find_smallest([5,4,3,2,1],"index"),4)
        test.assert_equals(find_smallest([ 8, 0, 9],"index"),1)
        test.assert_equals(find_smallest([ 8, 0, 9],"value"),0)
        test.assert_equals(find_smallest([ 1, 1, 0, 0, 1, 1],"value"),0)
        test.assert_equals(find_smallest([ 1, 1, 0, 0, 1, 1],"index"),2)
        test.assert_equals(find_smallest([0], 'value'), 0)
        test.assert_equals(find_smallest([0], 'index'), 0)


'''
Task 5:

Write a method, that gets an array of integer-numbers and return an array of the averages of each integer-number and his follower, if there is one.

Example:

Input:  [ 1, 3, 5, 1, -10]
Output:  [ 2, 4, 3, -4.5]
'''

# Solution:
def averages(arr):
    
    result_list = []
    first_value = None
    
    if arr is not None:
        
        for i in range(len(arr)):
            if first_value is not None:
                result_list.append((first_value + arr[i]) / 2)
            first_value = arr[i]
        return  result_list
    
    else:
        return []
    
# Tests:
import codewars_test as test
from solution import averages

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        tests = (
            ([2, 2, 2, 2], [2, 2, 2, 2, 2]),
            ([0, 0, 0, 0], [2, -2, 2, -2, 2]),
            ([2, 4, 3, -4.5], [1, 3, 5, 1, -10]),
            ([], [])
        )
        
        for exp, inp in tests:
            test.assert_equals(averages(inp), exp)

'''
Task 6:

The Format

Phone numbers are stored as strings and comprise 11 digits, eg '02078834982' and must always start with a 0.
However, something strange has happened and now all of the phone numbers contain lots of random characters, whitespace and some are not phone numbers at all!

For example,  '02078834982' has somehow become 'efRFS:)0207ERGQREG88349F82!' and there are lots more lines that we need to check.
'''

# Solution:
def is_it_a_num(s: str) -> str:
    result_string = ''.join(filter(str.isdigit, s))
    if result_string != '' and result_string[0] == '0' and len(result_string) == 11:
        return result_string
    else:
        return "Not a phone number"
    
# Tests:
import codewars_test as test
from solution import is_it_a_num


@test.describe("is_it_a_num")
def test_group():
    @test.it("Should pass sample tests")
    def test_case():
        test.assert_equals(is_it_a_num("S:)0207ERGQREG88349F82!efRF)"), "02078834982")
        test.assert_equals(is_it_a_num("sjfniebienvr12312312312ehfWh"), "Not a phone number")
        test.assert_equals(is_it_a_num("0192387415456"), "Not a phone number")
        test.assert_equals(is_it_a_num("v   uf  f 0tt2eg qe0b 8rtyq4eyq564()(((((165"), "02084564165")
        test.assert_equals(is_it_a_num("stop calling me no I have never been in an accident"), "Not a phone number")

'''
Task 7:

Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. 
No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
[10, 343445353, 3453445, 3453545353453] should return 3453455.
'''

# Solution:
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

# Tests:
import codewars_test as test
from solution import sum_two_smallest_numbers

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(sum_two_smallest_numbers([5, 8, 12, 18, 22]), 13)
        test.assert_equals(sum_two_smallest_numbers([7, 15, 12, 18, 22]), 19)
        test.assert_equals(sum_two_smallest_numbers([25, 42, 12, 18, 22]), 30)

'''
Task 8:

You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

For example:
time = 3 ----> litres = 1
'''

# Solution:
def litres(time):
    need_water = int(time // 2)
    return need_water

# Tests:
import codewars_test as test
from solution import litres

@test.describe('Fixed tests')
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(litres(2), 1, 'should return 1 litre')
        test.assert_equals(litres(1.4), 0, 'should return 0 litres')
        test.assert_equals(litres(12.3), 6, 'should return 6 litres')
        test.assert_equals(litres(0.82), 0, 'should return 0 litres')
        test.assert_equals(litres(11.8), 5, 'should return 5 litres')
        test.assert_equals(litres(1787), 893, 'should return 893 litres')
        test.assert_equals(litres(0), 0, 'should return 0 litres')

'''
Task 9:

Given an array arr (numbers of days of absence for each employee) and a number s (total bonus) the function bonus(arr, s) 
will follow John's way and return an array of the fair bonuses of all employees in the same order as their numbers of days of absences.
'''

# Solution:

# Tests:

'''
Task 10:


'''

# Solution:

# Tests:

'''
Task 20:


'''

# Solution:

# Tests: