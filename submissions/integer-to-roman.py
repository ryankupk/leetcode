# https://leetcode.com/problems/integer-to-roman

class Solution:
    def intToRoman(self, num: int) -> str:
        
        # Define the Roman numeral symbols and their values
        symbols = [
            ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90),
            ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
        ]
        
        roman = ''
        
        # Iterate through the symbols
        for symbol, value in symbols:
            # While the number is greater than or equal to the current value
            while num >= value:
                roman += symbol  # Add the symbol to the result
                num -= value     # Subtract the value from the number
        
        return roman