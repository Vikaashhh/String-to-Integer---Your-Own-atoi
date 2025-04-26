class Solution:
    def myAtoi(self, s):
        s = s.strip()  # Step 1: Leading whitespaces hata do

        if not s:
            return 0

        sign = 1
        i = 0
        n = len(s)
        result = 0

        # Step 2: Check for '+' ya '-' sign
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1

        # Step 3: Process digit characters
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')  # Convert char to int
            result = result * 10 + digit
            i += 1

        result *= sign

        # Step 4: Clamp the result within 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result
    

if __name__ == "__main__":
    obj = Solution()
    s = "   -42"
    print("Converted Integer is:", obj.myAtoi(s))