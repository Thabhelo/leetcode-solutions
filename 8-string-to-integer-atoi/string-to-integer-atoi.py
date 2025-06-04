class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        i = 0
        # Step 1: Skip leading whitespace
        while i < len(s) and s[i] == ' ':
            i += 1

        # Step 2: Check for optional sign
        sign = 1
        if i < len(s) and s[i] == '-':
            sign *= -1
            i += 1
        elif i < len(s) and s[i] == '+':
            i += 1

        # Step 3: Convert digits to integer
        result = 0
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            # Check for overflow
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
            result = result * 10 + digit
            i += 1
        
        return sign * result