class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Ignore leading whitespace
        s = s.lstrip()
        
        # Handle empty string after stripping
        if not s:
            return 0
        
        # Step 2: Determine signedness
        sign = 1
        index = 0
        
        if s[0] == '-':
            sign = -1
            index = 1
        elif s[0] == '+':
            sign = 1
            index = 1
        
        # Step 3: Conversion - read digits
        result = 0
        
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            
            # Check for overflow before adding the digit
            # 32-bit signed integer range: [-2^31, 2^31 - 1]
            if result > (2**31 - 1 - digit) // 10:
                return 2**31 - 1 if sign == 1 else -2**31
            
            result = result * 10 + digit
            index += 1
        
        # Step 4: Apply sign and return
        result = sign * result
        
        # Step 5: Handle rounding (clamping to 32-bit range)
        if result < -2**31:
            return -2**31
        elif result > 2**31 - 1:
            return 2**31 - 1
        
        return result