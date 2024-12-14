# Approach:
# Use a stack to handle intermediate results of the expression.
# Iterate through the string while parsing numbers and applying operators.
# For multiplication and division, directly compute the result with the previous number on the stack.
# For addition and subtraction, push the number (positive or negative) onto the stack.
# Finally, sum up the values in the stack to get the result.

# Time Complexity: O(N), where N is the length of the string. Each character is processed once.
# Space Complexity: O(N) for the stack, which stores the intermediate results.
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: Handling spaces and order of operations required attention.

class Solution:
    def calculate(self, s: str) -> int:
        # Initialize variables
        stack = []  # Stack to store numbers
        current_num = 0  # To build multi-digit numbers
        operation = '+'  # Default to addition for the first number
        
        # Iterate through the string
        for i, char in enumerate(s):
            # If the character is a digit, build the number
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            
            # If the character is an operator or end of string, process the current number
            if char in "+-*/" or i == len(s) - 1:
                # Apply the last operation
                if operation == '+':
                    stack.append(current_num)  # Push positive number
                elif operation == '-':
                    stack.append(-current_num)  # Push negative number
                elif operation == '*':
                    stack.append(stack.pop() * current_num)  # Perform multiplication
                elif operation == '/':
                    stack.append(int(stack.pop() / current_num))  # Perform division (truncate toward zero)
                
                # Reset for the next number and update operation
                current_num = 0
                operation = char
        
        # Return the sum of values in the stack
        return sum(stack)
