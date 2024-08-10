"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_thai(self, number: int) -> str:
        
        if number < 0:
            return "number can not less than 0"
        
        thai_digits = {
            "0": "ศูนย์", "1": "หนึ่ง", "2": "สอง", "3": "สาม", "4": "สี่",
            "5": "ห้า", "6": "หก", "7": "เจ็ด", "8": "แปด", "9": "เก้า"
        }
    
        thai_place_values = {
            1: "",  # Units place doesn't have a special name
            10: "สิบ",
            100: "ร้อย",
            1000: "พัน",
            10000: "หมื่น",
            100000: "แสน",
            1000000: "ล้าน",
            10000000: "สิบล้าน",
        }
        
        if number == 0:
            return thai_digits["0"]
        
        if number == 10_000_000:
            return thai_place_values[number]
        
        thai_word = ""
        
        digits = str(number)[::-1]  # Reverse the number string for place value

        for i in range(len(digits)):
            digit = digits[i]
            place_value = 10 ** i

            if digit == "0":
                continue

            # Handling for "หนึ่ง" in tens place ("สิบ" instead of "หนึ่งสิบ")
            if i == 1 and digit == "1":
                thai_word = thai_place_values[place_value] + thai_word
            # Handling for "สอง" in tens place ("ยี่สิบ" instead of "สองสิบ")
            elif i == 1 and digit == "2":
                thai_word = "ยี่" + thai_place_values[place_value] + thai_word
            # Handling for "เอ็ด" in units place only after tens place
            elif i == 0 and digit == "1" and number > 10:
                thai_word = "เอ็ด" + thai_word
            # Most cases for each place value
            else:
                thai_word = thai_digits[digit] + thai_place_values[place_value] + thai_word
        
        return thai_word
    
    
solution = Solution()
    
# Test case 1: Positive integer
assert solution.number_to_thai(101) == "หนึ่งร้อยเอ็ด", \
    f"Case 1, Thai word expected: หนึ่งร้อยเอ็ด, got: {solution.number_to_thai(101)}"

# Test case 2: Positive integer
assert solution.number_to_thai(6354) == "หกพันสามร้อยห้าสิบสี่", \
    f"Case 2, Thai word expected: หกพันสามร้อยห้าสิบสี่, got: {solution.number_to_thai(6354)}"

# Test case 3: Positive integer
assert solution.number_to_thai(9048025) == "เก้าล้านสี่หมื่นแปดพันยี่สิบห้า", \
    f"Case 3, Thai word expected: เก้าล้านสี่หมื่นแปดพันยี่สิบห้า, got: {solution.number_to_thai(9048025)}"
    
# Test case 4: Minimun Positive integer
assert solution.number_to_thai(0) == "ศูนย์", \
    f"Case 4, Thai word expected: ศูนย์, got: {solution.number_to_thai(0)}"
    
# Test case 5: Maximum Positive integer
assert solution.number_to_thai(10_000_000) == "สิบล้าน", \
    f"Case 5, Thai word expected: สิบล้าน, got: {solution.number_to_thai(10_000_000)}"

# Test case 6: Negative integer
assert solution.number_to_thai(-1) == "number can not less than 0", \
    f"Case 6, Expected: number can not less than 0, got: {solution.number_to_thai(-1)}"

print("All test cases passed!")
