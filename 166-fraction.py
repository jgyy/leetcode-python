class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        if denominator == 0:
            return 'NaN'
        if numerator % denominator == 0:
            return str(numerator // denominator)

        if numerator < 0 and denominator > 0 or numerator > 0 and denominator < 0:
            sign = '-'
        else:
            sign = ''

        numerator, denominator = abs(numerator), abs(denominator)
        integer = numerator // denominator
        numerator %= denominator
        decimal = []
        seen = {}
        while numerator != 0:
            if numerator in seen:
                decimal.insert(seen[numerator], '(')
                decimal.append(')')
                break
            seen[numerator] = len(decimal)
            numerator *= 10
            decimal.append(str(numerator // denominator))
            numerator %= denominator
        return sign + str(integer) + '.' + ''.join(decimal)


if __name__ == '__main__':
    print(Solution().fractionToDecimal(1, 2))
    print(Solution().fractionToDecimal(2, 1))
    print(Solution().fractionToDecimal(2, 3))
    print(Solution().fractionToDecimal(4, 333))
    print(Solution().fractionToDecimal(1, 5))
    print(Solution().fractionToDecimal(1, 6))
    print(Solution().fractionToDecimal(1, 7))
    print(Solution().fractionToDecimal(1, 8))
    print(Solution().fractionToDecimal(1, 9))
    print(Solution().fractionToDecimal(1, 10))
    print(Solution().fractionToDecimal(1, 11))
    print(Solution().fractionToDecimal(1, 12))
    print(Solution().fractionToDecimal(1, 13))
    print(Solution().fractionToDecimal(1, 14))
    print(Solution().fractionToDecimal(1, 15))
    print(Solution().fractionToDecimal(1, 16))
    print(Solution().fractionToDecimal(1, 17))
    print(Solution().fractionToDecimal(1, 18))
    print(Solution().fractionToDecimal(1, 19))
    print(Solution().fractionToDecimal(1, 20))
    print(Solution().fractionToDecimal(1, 21))
    print(Solution().fractionToDecimal(1, 22))
    print(Solution().fractionToDecimal(1, 23))
    print(Solution().fractionToDecimal(1, 24))
    print(Solution().fractionToDecimal(1, 25))
    print(Solution().fractionToDecimal(1, 26))
    print(Solution().fractionToDecimal(1, 27))
    print(Solution().fractionToDecimal(1, 28))
    print(Solution().fractionToDecimal(1, 29))
    print(Solution().fractionToDecimal(1, 30))
    print(Solution().fractionToDecimal(1, 31))
    print(Solution().fractionToDecimal(1, 32))
    print(Solution().fractionToDecimal(1, 33))
    print(Solution().fractionToDecimal(1, 34))
    print(Solution().fractionToDecimal(1, 35))
    print(Solution().fractionToDecimal(1, 36))
