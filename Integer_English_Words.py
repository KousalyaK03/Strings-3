# Approach:
# Break the number into groups of three digits (thousands, millions, etc.).
# Use helper arrays to map numbers to words for ones, tens, and teens.
# Construct the English words representation by processing each group recursively.
# Handle special cases like zero separately.

# Time Complexity: O(N) where N is the number of digits in the number (processing each digit).
# Space Complexity: O(1) since the space used is constant (arrays for mapping numbers to words).
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No major issues.

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"  # Special case for zero

        # Arrays to map numbers to words
        below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                    "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        # Helper function to convert a number < 1000 into words
        def three_digit_to_words(n):
            if n == 0:
                return ""
            elif n < 20:
                return below_20[n]
            elif n < 100:
                return tens[n // 10] + (" " + below_20[n % 10] if n % 10 != 0 else "")
            else:
                return below_20[n // 100] + " Hundred" + (" " + three_digit_to_words(n % 100) if n % 100 != 0 else "")

        # Process the number group by group
        res = []
        for i in range(len(thousands)):
            if num % 1000 != 0:
                res.append(three_digit_to_words(num % 1000) + (f" {thousands[i]}" if thousands[i] else ""))
            num //= 1000  # Move to the next group of three digits

        # Join all parts in reverse order
        return " ".join(reversed(res)).strip()

