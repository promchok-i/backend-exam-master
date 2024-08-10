"""
เขียบนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 4

[Example 2]
input = []
output = list can not blank
"""


class Solution:

    def find_max_index(self, numbers: list) -> int | str:

        if len(numbers) < 1:
            return "list can not blank"
        
        max_number_index = 0
        max_number = numbers[0]
        
        for i in range(1, len(numbers)):
            if max_number < numbers[i]:
                max_number_index = i
                max_number = numbers[i]
        
        return max_number_index
    

solution = Solution()

# Test case 1: Max number at last index
assert solution.find_max_index([1, 3, 5, 7]) == 3, \
    f"Case 1, Maximum number at index expected: 3, got: {solution.find_max_index([1, 3, 5, 7])}"

# Test case 2: Max number at start index
assert solution.find_max_index([10, 9, 8, 7, 6, 10]) == 0, \
    f"Case 2, Maximum number at index expected: 0, got: {solution.find_max_index([10, 9, 8, 7, 6])}"

# Test case 3: Max number at Middle index
assert solution.find_max_index([2, 5, 8, 7, 6, 4]) == 2, \
    f"Case 3, Maximum number at index expected: 2, got: {solution.find_max_index([2, 5, 8, 7, 6, 4])}"
    
# Test case 4: 1 Item in List
assert solution.find_max_index([123]) == 0, \
    f"Case 4, Maximum number at index expected: 0, got: {solution.find_max_index([123])}"

# Test case 5: Empty List
assert solution.find_max_index([]) == "list can not blank", \
    f"Case 5, Expected: list can not blank, got: {solution.find_max_index([])}"

print("All test cases passed!")
