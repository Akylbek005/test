import logging


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ''
        sl = list(s)
        print(sl)
        for i in range(0, len(s), numRows+1):
            res += sl.pop(i)
        return 'None'


if __name__ == '__main__':
    s = 'PAYPALISHIRING'
    numRows = 3
    solution = Solution()
    result = solution.convert(s, numRows)
    print(result)
