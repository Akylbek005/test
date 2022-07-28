from functools import reduce


class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n if x != 0 else 1


if __name__ == '__main__':
    x_ = 2.0
    n_ = 10
    solution = Solution()
    res = solution.myPow(x_, n_)
    print(res)


"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n != 0:
            result = x
            if n < 0:
                return x ** n
            for _ in range(n - 1):
                result *= x
            return result
        return 1
        
    
        if n != 0:
            result = reduce(lambda a, b: a * b, [x for _ in range(n)]) if n > 0 else x ** n
            return result
        return 1
        
        
        result = reduce(lambda a, b: a * b, [x for _ in range(n)]) if n > 0 else x ** n
        return 1 if n == 0 else result
        
        
        res = x
        if n == 0:
            res = 1

        elif 0 < n:
            for _ in range(n - 1):
                res *= x

        elif 0 > n:
            res = x ** n

        return res
"""
