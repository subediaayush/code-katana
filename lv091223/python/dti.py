class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        quotient = 0
        positive = (dividend <= 0 and divisor <= 0) or (dividend >= 0 and divisor >= 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        if (divisor == 1):
            quotient = dividend
        else:
            while dividend >= divisor:
                tmp = divisor
                multiplier = 1
                while dividend >= tmp:
                    dividend -= tmp
                    quotient += multiplier
                    multiplier += multiplier
                    tmp += tmp

        quotient = quotient if positive else -quotient
        return min(2**31 - 1, max(-2**31, quotient))
        
print(Solution().divide(50,-5))