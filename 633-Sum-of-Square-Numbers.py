class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = int(math.sqrt(c))
        b = 0
        while b <= a:
            if b * b + a * a == c:
                return True
            if b * b + a * a < c:
                b += 1
            else:
                a -= 1
        return False