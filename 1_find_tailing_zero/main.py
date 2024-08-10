"""
เขียบนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


class Solution:

    def find_tailing_zeroes(self, number: int) -> int | str:
        
        if number < 0:
            return "number can not be negative"
        
        count_zeros = 0
        while number > 0:
            # Number of 5 in factorial equal to number of trailing zeros
            number = number // 5
            count_zeros += number
            
        return count_zeros

        
solution = Solution()

# Test case 1: Zero integer
assert solution.find_tailing_zeroes(0) == 0, \
    f"Case 1, Number of zeros expected: 0, got: {solution.find_tailing_zeroes(0)}"

# Test case 2: Positive integer
assert solution.find_tailing_zeroes(7) == 1, \
    f"Case 2, Number of zeros expected: 1, got: {solution.find_tailing_zeroes(7)}"

# Test case 3: Positive integer
assert solution.find_tailing_zeroes(30) == 7, \
    f"Case 3, Number of zeros expected: 7, got: {solution.find_tailing_zeroes(30)}"
    
# Test case 4: Positive integer
assert solution.find_tailing_zeroes(1000) == 249, \
    f"Case 4, Number of zeros expected: 249, got: {solution.find_tailing_zeroes(1000)}"

# Test case 5: Negative integer
assert solution.find_tailing_zeroes(-10) == "number can not be negative", \
    f"Case 5, Expected: number can not be negative, got: {solution.find_tailing_zeroes(-10)}"

print("All test cases passed!")
