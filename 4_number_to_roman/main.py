"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_roman(self, number: int) -> str:
        
        if number < 0:
            return "number can not less than 0"
        
        roman_dict = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }
        
        roman = ""
        
        # Create roman from descending order number.
        for key, value in roman_dict.items():
            if number // key:
                count = number // key
                roman += (value * count)
                number = number % key
                
        return roman
    
    
solution = Solution()

# Test case 1: Positive integer
assert solution.number_to_roman(101) == "CI", \
    f"Case 1, Roman expected: CI, got: {solution.number_to_roman(101)}"

# Test case 2: Positive integer
assert solution.number_to_roman(2024) == "MMXXIV", \
    f"Case 2, Roman expected: MMXXIV, got: {solution.number_to_roman(2024)}"

# Test case 3: Positive integer
assert solution.number_to_roman(4) == "IV", \
    f"Case 3, Roman expected: IV, got: {solution.number_to_roman(4)}"

# Test case 4: Negative integer
assert solution.number_to_roman(-1) == "number can not less than 0", \
    f"Case 4, Expected: number can not less than 0, got: {solution.number_to_roman()}"

print("All test cases passed!")
